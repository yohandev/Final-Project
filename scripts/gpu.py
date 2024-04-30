# Simulates the RP2040 GPU. Talks to the PSoC over Serial
from pyrender import Viewer, Scene, Mesh, Primitive
from threading import Thread
from serial import Serial
from enum import Enum
from time import sleep
from struct import unpack

class PayloadType(Enum):
    PACKET_OVER = 0x80
    UPLOAD_MESH = 0x81
    CLEAR_BUFFER = 0x82
    SWAP_BUFFER = 0x83
    SET_CAMERA = 0x84
    DRAW_INSTANCED = 0x85
    DRAW_INSTANCED_QUAT = 0x86

scene = Scene()
viewer = Viewer.__new__(Viewer)

meshes = {}     # Meshes submitted from PSoC
cmdbuf = []     # Commands submitted from PSoC that are yet to be flushed
flush = False   # Whether or not the command buffer should be processed yet

def main():
    global cmdbuf, flush

    # Give UI thread some time to boot up
    sleep(0.5)
    
    with Serial("/dev/tty.usbmodem1103", 115200) as serial:
        sleep(0.6)
        serial.write(b'READY')
        while True:
            header = serial.read()
            # Oops, this was a print message!
            if header.isascii():
                print(chr(ord(header)), end="")
            # Otherwise parse the packet
            else:
                parse_packet(PayloadType(ord(header)), serial)
            
            # Process rendering commands
            if not flush:
                continue
            with viewer.render_lock:
                for (cmd, args) in cmdbuf:
                    pass
                cmdbuf = []
                flush = False


def parse_packet(header: PayloadType, serial: Serial):
    # Parsing utilities
    def pairwise(i):
        a = iter(i)
        return zip(a, a)
    read_usize = lambda: int.from_bytes(serial.read(4), "little")
    read_u16_array = lambda len: [unpack("h", bytes(b)) for b in pairwise(serial.read(len * 2))]
    read_vec3 = lambda: unpack("3f", serial.read(12))
    read_vec4 = lambda: unpack("4f", serial.read(16))
    packet_over = lambda: PayloadType(ord(serial.read())) == PayloadType.PACKET_OVER
    
    # == Upload Mesh ==
    if header == PayloadType.UPLOAD_MESH:
        id = read_usize()
        print(f"Uploading Mesh #{id}")
        num_vertices = read_usize()
        print(f"# Vertices: {num_vertices}")
        vertices = read_u16_array(num_vertices * 3)
        num_faces = read_usize()
        print(f"# Faces: {num_faces}")
        indices = read_u16_array(num_faces * 3)
        num_colors = read_usize()
        print(f"# Colors: {num_colors}")
        colors = read_u16_array(num_colors * 2)
        print("Unpacking...")

        # Unpack and store mesh
        vertices = [float(v) / (1 << 8) for (v,) in vertices]
        # TODO: colors
        meshes[id] = Mesh([Primitive(positions=vertices, indices=indices, mode=4)])

        with viewer.render_lock:
            scene.add(meshes[id])

        assert packet_over()
    # == Clear Buffer ==
    elif header == PayloadType.CLEAR_BUFFER:
        assert packet_over()
    # == Swap Buffer ==
    elif header == PayloadType.SWAP_BUFFER:
        global flush
        flush = True
        assert packet_over()
    # == Set Camera ==
    elif header == PayloadType.SET_CAMERA:
        pos = read_vec3()
        rot = read_vec3()

        cmdbuf.append((PayloadType.SET_CAMERA, (pos, rot)))

        assert packet_over()
    # == Draw Instanced ==
    elif header == PayloadType.DRAW_INSTANCED:
        id = read_usize()
        num_instances = read_usize()
        pos = [read_vec3() for _ in range(num_instances)]
        rot = [read_vec3() for _ in range(num_instances)]

        cmdbuf.append((PayloadType.DRAW_INSTANCED, (pos, rot)))

        assert packet_over()
    # == Draw Instanced (Quaternions) ==
    elif header == PayloadType.DRAW_INSTANCED_QUAT:
        id = read_usize()
        num_instances = read_usize()
        pos = [read_vec3() for _ in range(num_instances)]
        rot = [read_vec4() for _ in range(num_instances)]

        cmdbuf.append((PayloadType.DRAW_INSTANCED_QUAT, (pos, rot)))

        assert packet_over()
    else:
        raise ValueError(f"Unexpected header {header}!")

# Logic thread
Thread(target=main).start()
# UI thread
viewer.__init__(scene, use_raymond_lighting=True)