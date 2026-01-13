import maya.cmds as cmds
import maya.mel as mel


def limb_ui():
    # check to see if our window exists
    if cmds.window('AdvancedClavicleRigUI', exists=True):
        cmds.deleteUI('AdvancedClavicleRigUI')

    # create our window
    window = cmds.window('AdvancedClavicleRigUI', title='Advanced Clavicle Rig', width=455,
                         height=45, sizeable=False, maximizeButton=False)

    # create main layout
    main_layout = cmds.columnLayout(width=455, height=533)

    # add frame layouts
    help_area = help_area_frame(window, main_layout)
    data_dict = build_data_frame(window, main_layout)
    arg_dict = build_axis_frame(window, main_layout)

    command_dict = data_dict.copy()
    command_dict.update(arg_dict)

    # add build/close buttons
    button_grid(window, main_layout, command_dict, arg_dict)

    # show window
    cmds.showWindow(window)


def help_area_frame(window, main_layout):
    data_frame = cmds.frameLayout(label='Help', width=453, height=118,
                                  collapsable=True, parent=main_layout,
                                  collapseCommand=lambda: collapse_cmd(
                                      window, data_frame, 118),
                                  expandCommand=lambda: expand_cmd(
                                      window, data_frame, 118))

    rcl = cmds.rowColumnLayout(numberOfColumns=1,
                               columnWidth=[(1, 455)],
                               columnOffset=[(1, 'both', 5)], parent=data_frame)

    cmds.text(label='"shoulder_guide" = shoulder_jnt.',
              align='left', parent=rcl)
    cmds.text(label='"scap1_guide" and "scap2_guide" are the top and the bottom of the scapula.',
              align='left', parent=rcl)
    cmds.text(label='"trap1_guide" is the end of the trapezius over the shoulder.',
              align='left', parent=rcl)
    cmds.text(label='"trap2_guide" is the beginning of the trapezius at the edge of the neck.',
              align='left', parent=rcl)
    cmds.text(label='"pec1_guide" is located right behind the nipple.',
              align='left', parent=rcl)
    cmds.text(label='"lat1_guide" is located at the same height with "pec1_guide" at the edge of the body.',
              align='left', parent=rcl)
    cmds.text(label='Clavicle Secondary Axis is the axis around which the clavicle rotates backwards.',
              align='left', parent=rcl)


def build_data_frame(window, main_layout):
    data_frame = cmds.frameLayout(label='Build Data', width=453, height=280,
                                  collapsable=True, parent=main_layout,
                                  collapseCommand=lambda: collapse_cmd(
                                      window, data_frame, 280),
                                  expandCommand=lambda: expand_cmd(
                                      window, data_frame, 280))

    rcl = cmds.rowColumnLayout(numberOfColumns=4,
                               columnWidth=[(1, 158), (2, 65), (3, 158), (4, 65)],
                               columnOffset=[(1, 'both', 5), (2, 'both', 0),
                                             (3, 'both', 5), (4, 'both', 0)], parent=data_frame)

    cmds.text(label='Guide', align='left', fn='boldLabelFont',
              height=30, parent=rcl)
    cmds.text(label='Load', align='left', fn='boldLabelFont',
              height=30, parent=rcl)

    cmds.text(label='Joint', align='left', fn='boldLabelFont',
              height=30, parent=rcl)
    cmds.text(label='Load', align='left', fn='boldLabelFont',
              height=30, parent=rcl)

    shoulder_guide_input = cmds.textField(height=30, parent=rcl, text='shoulder_guide')
    shoulder_guide_load = cmds.button(label='load sel.', height=30, parent=rcl,
                                      command=lambda x: load_sel(shoulder_guide_input))

    chest_jnt_input = cmds.textField(height=30, parent=rcl, text='chest_jnt')
    chest_jnt_load = cmds.button(label='load sel.', height=30, parent=rcl,
                                 command=lambda x: load_sel(chest_jnt_input))

    scap1_guide_input = cmds.textField(height=30, parent=rcl, text='scap1_guide')
    scap1_guide_load = cmds.button(label='load sel.', height=30, parent=rcl,
                                   command=lambda x: load_sel(scap1_guide_input))

    clavicle01_jnt_input = cmds.textField(height=30, parent=rcl, text='clavicle01_jnt')
    clavicle01_jnt_load = cmds.button(label='load sel.', height=30, parent=rcl,
                                      command=lambda x: load_sel(clavicle01_jnt_input))

    scap2_guide_input = cmds.textField(height=30, parent=rcl, text='scap2_guide')
    scap2_guide_load = cmds.button(label='load sel.', height=30, parent=rcl,
                                   command=lambda x: load_sel(scap2_guide_input))

    cmds.separator(style='none', parent=rcl)
    cmds.separator(style='none', parent=rcl)

    trap1_guide_input = cmds.textField(height=30, parent=rcl, text='trap1_guide')
    trap1_guide_load = cmds.button(label='load sel.', height=30, parent=rcl,
                                   command=lambda x: load_sel(trap1_guide_input))

    cmds.text(label='Side', align='left', fn='obliqueLabelFont',
              height=20, parent=rcl)
    cmds.separator(style='none', parent=rcl)

    trap2_guide_input = cmds.textField(height=30, parent=rcl, text='trap2_guide')
    trap2_guide_load = cmds.button(label='load sel.', height=30, parent=rcl,
                                   command=lambda x: load_sel(trap2_guide_input))

    side_input = cmds.textField(height=30, parent=rcl, text='L')
    cmds.separator(style='none', parent=rcl)

    pec1_guide_input = cmds.textField(height=30, parent=rcl, text='pec1_guide')
    pec1_guide_load = cmds.button(label='load sel.', height=30, parent=rcl,
                                  command=lambda x: load_sel(pec1_guide_input))

    cmds.text(label='Scapula Shrink Intensity', align='left', fn='obliqueLabelFont',
              height=20, parent=rcl)
    cmds.separator(style='none', parent=rcl)

    lat1_guide_input = cmds.textField(height=30, parent=rcl, text='lat1_guide')
    lat1_guide_load = cmds.button(label='load sel.', height=30, parent=rcl,
                                  command=lambda x: load_sel(lat1_guide_input))

    shrink_intensity_input = cmds.textField(height=30, parent=rcl, text='0.1')
    cmds.separator(style='none', parent=rcl)

    return_dict = {'shoulder_guide_input': shoulder_guide_input,
                   'chest_jnt_input': chest_jnt_input,
                   'scap1_guide_input': scap1_guide_input,
                   'clavicle01_jnt_input': clavicle01_jnt_input,
                   'scap2_guide_input': scap2_guide_input,
                   'trap1_guide_input': trap1_guide_input,
                   'trap2_guide_input': trap2_guide_input,
                   'side_input': side_input,
                   'pec1_guide_input': pec1_guide_input,
                   'lat1_guide_input': lat1_guide_input,
                   'shrink_intensity_input': shrink_intensity_input
                   }

    return return_dict


def build_axis_frame(window, main_layout):
    arg_frame = cmds.frameLayout(label='Build Axis', width=453, height=90,
                                 collapsable=True, parent=main_layout,
                                 collapseCommand=lambda: collapse_cmd(
                                     window, arg_frame, 90),
                                 expandCommand=lambda: expand_cmd(
                                     window, arg_frame, 90))

    baf_col = cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, 450)],
                                   columnOffset=[(1, 'both', 0)],
                                   parent=arg_frame)

    prcl = cmds.rowColumnLayout(numberOfColumns=4, height=60,
                                columnWidth=[(1, 150), (2, 110),
                                             (3, 110), (4, 50)],
                                columnOffset=[(1, 'both', 5), (2, 'both', 5),
                                              (3, 'both', 5), (4, 'both', 5)],
                                parent=baf_col)

    cmds.text(label='Primary Axis:', align='left', fn='boldLabelFont',
              height=30, parent=prcl)
    pa_col = cmds.radioCollection(numberOfCollectionItems=3, parent=prcl)
    px = cmds.radioButton(label='X', parent=prcl)
    py = cmds.radioButton(label='Y', parent=prcl)
    pz = cmds.radioButton(label='Z', parent=prcl)
    pa2_col = cmds.radioCollection(numberOfCollectionItems=3, parent=prcl)
    cmds.text(label='Clavicle Secondary Axis:', align='left', fn='boldLabelFont',
              height=30, parent=prcl)
    snx = cmds.radioButton(label='X', parent=prcl)
    sny = cmds.radioButton(label='Y', parent=prcl)
    snz = cmds.radioButton(label='Z', parent=prcl)
    cmds.radioCollection(pa_col, edit=True, select=px)
    cmds.radioCollection(pa2_col, edit=True, select=snz)

    axis_dict = {'primary_axis': pa_col,
                 'secondary_axis': pa2_col}

    return axis_dict


def button_grid(window, main_layout, command_dict, axis_dict):
    btn_col = cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, 453)],
                                   columnOffset=[(1, 'both', 0)],
                                   parent=main_layout)
    grid_layout = cmds.gridLayout(numberOfColumns=2, cellWidthHeight=(226, 40),
                                  parent=btn_col)
    build_btn = cmds.button(label='Build Rig', height=40, parent=grid_layout,
                            command=lambda x: build_rig_cmd(command_dict, axis_dict))
    close_btn = cmds.button(label='Clear Results', height=40, parent=grid_layout,
                            command=lambda x: clear_results_cmd(command_dict))


def collapse_cmd(window, frame_layout, height):
    window_height = cmds.window(window, query=True, height=True)
    frame_height = cmds.frameLayout(frame_layout, query=True, height=True)
    cmds.window(window, edit=True, height=window_height - height + 25)
    cmds.frameLayout(frame_layout, edit=True, height=frame_height - height + 25)


def expand_cmd(window, frame_layout, height):
    window_height = cmds.window(window, query=True, height=True)
    frame_height = cmds.frameLayout(frame_layout, query=True, height=True)
    cmds.window(window, edit=True, height=window_height + height - 25)
    cmds.frameLayout(frame_layout, edit=True, height=frame_height + height - 25)


def load_sel(text_field):
    sel = cmds.ls(sl=True)
    if len(sel):
        cmds.textField(text_field, edit=True, text=sel[0])


def build_rig_cmd(command_dict, axis_dict):
    shoulder_guide_input = cmds.textField(command_dict['shoulder_guide_input'], query=True, text=True)
    intersection_of_the_arms = cmds.textField(command_dict['chest_jnt_input'], query=True, text=True)
    scap1_guide_input = cmds.textField(command_dict['scap1_guide_input'], query=True, text=True)
    clavicle01 = cmds.textField(command_dict['clavicle01_jnt_input'], query=True, text=True)
    scap2_guide_input = cmds.textField(command_dict['scap2_guide_input'], query=True, text=True)
    trap1_guide_input = cmds.textField(command_dict['trap1_guide_input'], query=True, text=True)
    trap2_guide_input = cmds.textField(command_dict['trap2_guide_input'], query=True, text=True)
    side = cmds.textField(command_dict['side_input'], query=True, text=True)
    pec1_guide_input = cmds.textField(command_dict['pec1_guide_input'], query=True, text=True)
    lat1_guide_input = cmds.textField(command_dict['lat1_guide_input'], query=True, text=True)
    shrink_intensity_input = cmds.textField(command_dict['shrink_intensity_input'], query=True, text=True)

    primary_col = cmds.radioCollection(axis_dict['primary_axis'], query=True, sl=True)
    primary_axis_raw = cmds.radioButton(primary_col, query=True, label=True)
    secondary_col = cmds.radioCollection(axis_dict['secondary_axis'], query=True, sl=True)
    secondary_axis_raw = cmds.radioButton(secondary_col, query=True, label=True)

    if secondary_axis_raw == 'X':
        secondary_axis = 'rx'
    elif secondary_axis_raw == 'Y':
        secondary_axis = 'ry'
    elif secondary_axis_raw == 'Z':
        secondary_axis = 'rz'

    # Derivatives
    upstreamingjoint = cmds.pickWalk(intersection_of_the_arms, direction='down')[0]
    clavicle02 = cmds.pickWalk(clavicle01, direction='down')[0]
    armpoint = cmds.pickWalk(clavicle02, direction='down')[0]

    # Create new joints in place of locators using temporary pc:
    cmds.select(clear=True)
    cmds.joint(p=(0, 0, 0), name=side+'_scapRot_jntEnd')
    cmds.joint(p=(0, 0, 0), name=side+'_scap1_jnt')
    cmds.joint(p=(0, 0, 0), name=side+'_scap2_jntEnd')
    cmds.select(clear=True)
    cmds.joint(p=(0, 0, 0), name=side+'_trap1_jnt')
    cmds.joint(p=(0, 0, 0), name=side+'_trap2_jntEnd')
    cmds.select(clear=True)
    cmds.joint(p=(0, 0, 0), name=side+'_pec1_jnt')
    cmds.select(clear=True)
    cmds.joint(p=(0, 0, 0), name=side+'_lat1_jnt')
    cmds.select(clear=True)

    pc = cmds.parentConstraint(shoulder_guide_input, side+'_scapRot_jntEnd', mo=0)
    cmds.delete(pc)
    pc = cmds.parentConstraint(scap1_guide_input, side+'_scap1_jnt', mo=0)
    cmds.delete(pc)
    pc = cmds.parentConstraint(scap2_guide_input, side+'_scap2_jntEnd', mo=0)
    cmds.delete(pc)
    pc = cmds.parentConstraint(trap1_guide_input, side+'_trap1_jnt', mo=0)
    cmds.delete(pc)
    pc = cmds.parentConstraint(trap2_guide_input, side+'_trap2_jntEnd', mo=0)
    cmds.delete(pc)
    pc = cmds.parentConstraint(pec1_guide_input, side+'_pec1_jnt', mo=0)
    cmds.delete(pc)
    pc = cmds.parentConstraint(lat1_guide_input, side+'_lat1_jnt', mo=0)
    cmds.delete(pc)

    cmds.makeIdentity(side+'_scapRot_jntEnd', apply=True, rotate=True)
    cmds.select(side+'_scapRot_jntEnd')
    cmds.joint(e=True,  oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True)
    cmds.select(side+'_trap1_jnt')
    cmds.joint(e=True,  oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True)

    cmds.select(side+'_scap2_jntEnd')
    mel.eval("joint -e  -oj none -ch -zso;")
    cmds.select(side+'_trap2_jntEnd')
    mel.eval("joint -e  -oj none -ch -zso;")

    # Hierarchy
    cmds.parent(side+'_scapRot_jntEnd', armpoint)
    cmds.parent(side+'_trap1_jnt', clavicle02)
    grp = cmds.group(em=1, name=side+'_lat1_grp')
    cmds.parent(side+'_lat1_jnt', grp)
    grp = cmds.group(em=1, name=side+'_pec1_grp')
    cmds.parent(side+'_pec1_jnt', grp)

    # PrC, PC
    cmds.parentConstraint(intersection_of_the_arms, side + '_pec1_grp', mo=1)
    cmds.pointConstraint(clavicle02, intersection_of_the_arms, side + '_pec1_jnt', w=.5, skip="x", mo=1)
    cmds.pointConstraint(clavicle02, intersection_of_the_arms, side + '_lat1_jnt', w=.5, skip='y', sk='z', mo=1)

    # Controller
    cmds.ikHandle(sj=clavicle01, ee=clavicle02, n=side+'_clavicle_ikHandle', solver='ikSCsolver')
    offsetX = -3
    offsetZ = 3
    cmds.curve(p=[(-0.5+offsetX, 0, 1+offsetZ), (-0.5+offsetX, 0, 0+offsetZ),
                   (-1+offsetX, 0, 0+offsetZ), (0+offsetX, 0, -1+offsetZ),
                   (1+offsetX, 0, 0+offsetZ), (0.5+offsetX, 0, 0+offsetZ),
                   (0.5+offsetX, 0, 1+offsetZ), (-0.5+offsetX, 0, 1+offsetZ)], degree=1, name=side+'_clavicle_ctrl')
    grp = cmds.group(em=1, name=side+'_clavicle_ctrlGrp')
    cmds.parent(side+'_clavicle_ctrl', grp)
    cmds.rotate('-90deg', 0, '-45deg')
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    if side == 'R':
        cmds.scale(-1, 1, 1)

    pc = cmds.pointConstraint(side+'_clavicle_ikHandle', side+'_clavicle_ctrlGrp', mo=0)
    cmds.delete(pc)
    cmds.parentConstraint(side+'_clavicle_ctrl', side+'_clavicle_ikHandle', mo=1)

    cmds.setAttr (side+'_clavicle_ctrl' +'.rotateX',keyable = False, cb = False, lock = True)
    cmds.setAttr (side+'_clavicle_ctrl' +'.rotateY',keyable = False, cb = False, lock = True)
    cmds.setAttr (side+'_clavicle_ctrl' +'.rotateZ',keyable = False, cb = False, lock = True)
    cmds.setAttr (side+'_clavicle_ctrl' +'.scaleX',keyable = False, cb = False, lock = True)
    cmds.setAttr (side+'_clavicle_ctrl' +'.scaleY',keyable = False, cb = False, lock = True)
    cmds.setAttr (side+'_clavicle_ctrl' +'.scaleZ',keyable = False, cb = False, lock = True)
    cmds.setAttr (side+'_clavicle_ctrl' +'.visibility',keyable = False, cb = False, lock = True)

    # Locator
    if cmds.objExists('C_shoulderUp_loc') == 0:
        cmds.spaceLocator(name='C_shoulderUp_loc')
        cmds.parentConstraint(intersection_of_the_arms, 'C_shoulderUp_loc', mo=0)

    # Aim constraints
    wu_x = 0
    wu_y = 0
    wu_z = 0

    if primary_axis_raw == 'X':
        wu_x = 1
    elif primary_axis_raw == 'Y':
        wu_y = 1
    elif primary_axis_raw == 'Z':
        wu_z = 1

    cmds.aimConstraint(upstreamingjoint, side + '_trap1_jnt', mo=1, wut='objectrotation', wuo='C_shoulderUp_loc', wu=(wu_x, wu_y, wu_z))
    cmds.aimConstraint(upstreamingjoint, side + '_scapRot_jntEnd', mo=1, wut='objectrotation', wuo='C_shoulderUp_loc', wu=(wu_x, wu_y, wu_z))
    cmds.aimConstraint(intersection_of_the_arms, side + '_scap1_jnt', mo=1, wut='objectrotation', wuo='C_shoulderUp_loc', wu=(wu_x, wu_y, wu_z))

    # Scapula tweak
    cmds.createNode('multiplyDivide', n='scapulaMultiply'+side)
    cmds.createNode('plusMinusAverage', n='scapulaPlusMinus'+side)
    cmds.createNode('condition', n='scapulaCondition'+side)
    cmds.createNode('condition', n='scapulaCondition2'+side)

    cmds.setAttr('scapulaMultiply' + side + '.input1X', float(shrink_intensity_input))  # multiplier
    offset_t = cmds.getAttr(side + '_scap1_jnt.translate' + primary_axis_raw)
    cmds.setAttr('scapulaPlusMinus' + side + '.input1D[0]', offset_t)  # offset
    cmds.setAttr('scapulaCondition' + side + '.operation', 4)
    cmds.setAttr('scapulaCondition' + side + '.colorIfFalseR', offset_t)
    cmds.setAttr('scapulaCondition2' + side + '.operation', 2)
    cmds.setAttr('scapulaCondition2' + side + '.secondTerm', 0)
    cmds.setAttr('scapulaCondition2' + side+'.colorIfFalseR', 0)

    cmds.connectAttr(clavicle01+'.' + secondary_axis, 'scapulaMultiply' + side + '.input2X')
    cmds.connectAttr('scapulaMultiply' + side + '.ox', 'scapulaPlusMinus' + side + '.input1D[1]')
    cmds.connectAttr('scapulaPlusMinus' + side + '.o1', 'scapulaCondition' + side + '.colorIfTrueR')
    cmds.connectAttr(clavicle01 + '.' + secondary_axis, 'scapulaCondition' + side + '.firstTerm')
    cmds.connectAttr('scapulaCondition' + side + '.ocr', 'scapulaCondition2' + side + '.firstTerm')
    cmds.connectAttr('scapulaCondition' + side + '.ocr', 'scapulaCondition2' + side + '.colorIfTrueR')
    cmds.connectAttr('scapulaCondition2' + side + '.ocr', side + '_scap1_jnt.translate' + primary_axis_raw)


def clear_results_cmd(command_dict):
    side = cmds.textField(command_dict['side_input'], query=True, text=True)
    cmds.delete(side+'_scapRot_jntEnd')
    cmds.delete(side+'_trap1_jnt')
    cmds.delete(side+'_pec1_grp')
    cmds.delete(side+'_lat1_grp')
    if cmds.objExists('C_shoulderUp_loc'):
        cmds.delete('C_shoulderUp_loc')
    cmds.delete(side+'_clavicle_ctrlGrp')
    cmds.delete(side+'_clavicle_ikHandle')


limb_ui()
