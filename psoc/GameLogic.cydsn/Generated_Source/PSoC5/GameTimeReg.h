/*******************************************************************************
* File Name: GameTimeReg.h  
* Version 1.90
*
* Description:
*  This file containts Status Register function prototypes and register defines
*
* Note:
*
********************************************************************************
* Copyright 2008-2015, Cypress Semiconductor Corporation.  All rights reserved.
* You may use this file only in accordance with the license, terms, conditions, 
* disclaimers, and limitations in the end user license agreement accompanying 
* the software package with which this file was provided.
*******************************************************************************/

#if !defined(CY_STATUS_REG_GameTimeReg_H) /* CY_STATUS_REG_GameTimeReg_H */
#define CY_STATUS_REG_GameTimeReg_H

#include "cytypes.h"
#include "CyLib.h"

    
/***************************************
*     Data Struct Definitions
***************************************/

/* Sleep Mode API Support */
typedef struct
{
    uint8 statusState;

} GameTimeReg_BACKUP_STRUCT;


/***************************************
*        Function Prototypes
***************************************/

uint8 GameTimeReg_Read(void) ;
void GameTimeReg_InterruptEnable(void) ;
void GameTimeReg_InterruptDisable(void) ;
void GameTimeReg_WriteMask(uint8 mask) ;
uint8 GameTimeReg_ReadMask(void) ;


/***************************************
*           API Constants
***************************************/

#define GameTimeReg_STATUS_INTR_ENBL    0x10u


/***************************************
*         Parameter Constants
***************************************/

/* Status Register Inputs */
#define GameTimeReg_INPUTS              8


/***************************************
*             Registers
***************************************/

/* Status Register */
#define GameTimeReg_Status             (* (reg8 *) GameTimeReg_sts_sts_reg__STATUS_REG )
#define GameTimeReg_Status_PTR         (  (reg8 *) GameTimeReg_sts_sts_reg__STATUS_REG )
#define GameTimeReg_Status_Mask        (* (reg8 *) GameTimeReg_sts_sts_reg__MASK_REG )
#define GameTimeReg_Status_Aux_Ctrl    (* (reg8 *) GameTimeReg_sts_sts_reg__STATUS_AUX_CTL_REG )

#endif /* End CY_STATUS_REG_GameTimeReg_H */


/* [] END OF FILE */
