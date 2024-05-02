// Origin mesh: ./assets/asteroid.ply
// Converted using scripts/meshgen.py
#include "gpu.h"
#include "num.h"

static const i16 VERTICES[] = {
    153, -27, 180,
    -81, -201, 189,
    -246, -97, 5,
    -246, 59, 97,
    101, 175, -324,
    141, -296, 110,
    139, -289, -109,
    -53, -308, -174,
    -139, -209, -22,
    150, -129, -163,
    136, -74, 16,
    274, 43, -84,
    -5, -4, 361,
    -102, -106, 119,
    184, -3, -271,
    -87, -85, -295,
    159, 159, 192,
    -67, 153, 236,
    0, 326, 0,
    30, 229, 129,
    -242, 178, -172,
    21, 174, -231,
};

static const u16 INDICES[] = {
    7, 5, 1,
    0, 5, 10,
    7, 1, 8,
    1, 0, 12,
    2, 13, 3,
    1, 12, 13,
    9, 14, 11,
    3, 17, 19,
    18, 11, 21,
    11, 4, 21,
    21, 20, 18,
    20, 19, 18,
    20, 3, 19,
    17, 16, 19,
    19, 16, 18,
    16, 11, 18,
    14, 4, 11,
    15, 21, 4,
    15, 20, 21,
    2, 3, 20,
    13, 17, 3,
    13, 12, 17,
    12, 16, 17,
    0, 10, 16,
    10, 11, 16,
    14, 15, 4,
    14, 9, 15,
    15, 2, 20,
    15, 8, 2,
    12, 0, 16,
    10, 9, 11,
    6, 7, 9,
    7, 15, 9,
    7, 8, 15,
    8, 13, 2,
    8, 1, 13,
    10, 6, 9,
    10, 5, 6,
    5, 7, 6,
    1, 5, 0,
};

static const struct ColorRange COLORS[] = {
    { 0, { .r=0, .g=0, .b=0 }},
};

const struct Mesh ASSET_ASTEROID_MESH = {
    .vertices = VERTICES,
    .indices = INDICES,
    .colors = COLORS,

    .num_vertices = 22,
    .num_faces = 40,
    .num_colors = 1,
};