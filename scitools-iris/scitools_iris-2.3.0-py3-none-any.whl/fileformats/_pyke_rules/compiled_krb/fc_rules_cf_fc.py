# fc_rules_cf_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def fc_default(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    build_cube_metadata(engine)
    engine.rule_triggered.add(rule.name)
    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_rotated_latitude_longitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_ROTATED_LAT_LON):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_rotated_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_latitude_longitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_LAT_LON):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_coordinate_system(cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_transverse_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_TRANSVERSE):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_transverse_mercator_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_MERCATOR):
          if has_supported_mercator_parameters(engine, context.lookup_data('grid_mapping')):
            cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
            coordinate_system = build_mercator_coordinate_system(engine, cf_grid_var)
            engine.provides['coordinate_system'] = coordinate_system
            engine.assert_('facts_cf', 'provides',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_stereographic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_STEREO):
          if has_supported_stereographic_parameters(engine, context.lookup_data('grid_mapping')):
            cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
            coordinate_system = build_stereographic_coordinate_system(engine, cf_grid_var)
            engine.provides['coordinate_system'] = coordinate_system
            engine.assert_('facts_cf', 'provides',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_lambert_conformal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_LAMBERT_CONFORMAL):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_lambert_conformal_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_lambert_azimuthal_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_LAMBERT_AZIMUTHAL):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_lambert_azimuthal_equal_area_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_albers_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_ALBERS):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_albers_equal_area_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_vertical_perspective(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_VERTICAL):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = \
                      build_vertical_perspective_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_geostationary(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'),
           CF_GRID_MAPPING_GEOSTATIONARY):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = \
                      build_geostationary_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_coordinate_latitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_latitude(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_coordinate_longitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_longitude(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_projection_x_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_projection_x_coordinate(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_projection_y_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_projection_y_coordinate(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_coordinate_time(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_time(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_coordinate_time_period(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_time_period(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_label_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'label', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        cf_coord_var = engine.cf_var.cf_group.labels[context.lookup_data('coordinate')]
        build_auxiliary_coordinate(engine, cf_coord_var)
        engine.rule_triggered.add(rule.name)
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_time(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_time(engine, context.lookup_data('coordinate')):
          cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
          build_auxiliary_coordinate(engine, cf_coord_var)
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_time_period(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_time_period(engine, context.lookup_data('coordinate')):
          cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
          build_auxiliary_coordinate(engine, cf_coord_var)
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_latitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_latitude(engine, context.lookup_data('coordinate')):
          if not is_rotated_latitude(engine, context.lookup_data('coordinate')):
            cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
            build_auxiliary_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_LAT)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_latitude_rotated(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_latitude(engine, context.lookup_data('coordinate')):
          if is_rotated_latitude(engine, context.lookup_data('coordinate')):
            cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
            build_auxiliary_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_GRID_LAT)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_longitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_longitude(engine, context.lookup_data('coordinate')):
          if not is_rotated_longitude(engine, context.lookup_data('coordinate')):
            cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
            build_auxiliary_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_LON)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_longitude_rotated(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_longitude(engine, context.lookup_data('coordinate')):
          if is_rotated_longitude(engine, context.lookup_data('coordinate')):
            cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
            build_auxiliary_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_GRID_LON)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if not is_time(engine, context.lookup_data('coordinate')):
          if not is_time_period(engine, context.lookup_data('coordinate')):
            if not is_latitude(engine, context.lookup_data('coordinate')):
              if not is_longitude(engine, context.lookup_data('coordinate')):
                cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
                build_auxiliary_coordinate(engine, cf_coord_var)
                engine.rule_triggered.add(rule.name)
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_cell_measure(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'cell_measure', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        cf_coord_var = engine.cf_var.cf_group.cell_measures[context.lookup_data('coordinate')]
        build_cell_measures(engine, cf_coord_var)
        engine.rule_triggered.add(rule.name)
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_latitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if not is_rotated_latitude(engine, context.lookup_data('coordinate')):
              cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
              build_dimension_coordinate(engine, cf_coord_var,
              coord_name=CF_VALUE_STD_NAME_LAT,
              coord_system=engine.provides['coordinate_system'])
              engine.rule_triggered.add(rule.name)
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_latitude_rotated(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if is_rotated_latitude(engine, context.lookup_data('coordinate')):
              cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
              build_dimension_coordinate(engine, cf_coord_var,
              coord_name=CF_VALUE_STD_NAME_GRID_LAT,
              coord_system=engine.provides['coordinate_system'])
              engine.rule_triggered.add(rule.name)
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_longitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if not is_rotated_longitude(engine, context.lookup_data('coordinate')):
              cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
              build_dimension_coordinate(engine, cf_coord_var,
              coord_name=CF_VALUE_STD_NAME_LON,
              coord_system=engine.provides['coordinate_system'])
              engine.rule_triggered.add(rule.name)
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_longitude_rotated(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if is_rotated_longitude(engine, context.lookup_data('coordinate')):
              cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
              build_dimension_coordinate(engine, cf_coord_var,
              coord_name=CF_VALUE_STD_NAME_GRID_LON,
              coord_system=engine.provides['coordinate_system'])
              engine.rule_triggered.add(rule.name)
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_latitude_nocs(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany607_worked = True
        with engine.lookup('facts_cf', 'provides', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany607_worked = False
            if not notany607_worked: break
        if notany607_worked:
          notany609_worked = True
          with engine.lookup('facts_cf', 'provides', context, \
                             rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              notany609_worked = False
              if not notany609_worked: break
          if notany609_worked:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_LAT,
            coord_system=None)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_longitude_nocs(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany630_worked = True
        with engine.lookup('facts_cf', 'provides', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany630_worked = False
            if not notany630_worked: break
        if notany630_worked:
          notany632_worked = True
          with engine.lookup('facts_cf', 'provides', context, \
                             rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              notany632_worked = False
              if not notany632_worked: break
          if notany632_worked:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_LON,
            coord_system=None)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_transverse_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_transverse_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_lambert_conformal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_lambert_conformal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_stereographic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_stereographic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_lambert_azimuthal_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_lambert_azimuthal_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_albers_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_albers_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_vertical_perspective(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_vertical_perspective(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_geostationary(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_geostationary(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_time(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
        build_dimension_coordinate(engine, cf_coord_var)
        engine.rule_triggered.add(rule.name)
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_time_period(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
        build_dimension_coordinate(engine, cf_coord_var)
        engine.rule_triggered.add(rule.name)
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_default_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany998_worked = True
        with engine.lookup('facts_cf', 'provides', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany998_worked = False
            if not notany998_worked: break
        if notany998_worked:
          cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
          build_dimension_coordinate(engine, cf_coord_var)
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_attribute_ukmo__um_stash_source(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    if hasattr(engine.cf_var, 'ukmo__um_stash_source') or hasattr(engine.cf_var, 'um_stash_source'):
      attr_value = getattr(engine.cf_var, 'um_stash_source', None) or getattr(engine.cf_var, 'ukmo__um_stash_source')
      engine.cube.attributes['STASH'] = pp.STASH.from_msi(attr_value)
      engine.rule_triggered.add(rule.name)
      rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_attribute_ukmo__process_flags(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    if hasattr(engine.cf_var, 'ukmo__process_flags'):
      attr_value = engine.cf_var.ukmo__process_flags
      engine.cube.attributes['ukmo__process_flags'] = tuple([x.replace("_", " ") for x in attr_value.split(" ")])
      engine.rule_triggered.add(rule.name)
      rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_atmosphere_hybrid_height_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'atmosphere_hybrid_height_coordinate':
          engine.requires['formula_type'] = 'atmosphere_hybrid_height_coordinate'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_atmosphere_hybrid_sigma_pressure_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'atmosphere_hybrid_sigma_pressure_coordinate':
          engine.requires['formula_type'] = 'atmosphere_hybrid_sigma_pressure_coordinate'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_ocean_sigma_z_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'ocean_sigma_z_coordinate':
          engine.requires['formula_type'] = 'ocean_sigma_z_coordinate'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_ocean_sigma_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'ocean_sigma_coordinate':
          engine.requires['formula_type'] = 'ocean_sigma_coordinate'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_ocean_s_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'ocean_s_coordinate':
          engine.requires['formula_type'] = 'ocean_s_coordinate'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_ocean_s_coordinate_g1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'ocean_s_coordinate_g1':
          engine.requires['formula_type'] = 'ocean_s_coordinate_g1'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_ocean_s_coordinate_g2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'ocean_s_coordinate_g2':
          engine.requires['formula_type'] = 'ocean_s_coordinate_g2'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_terms(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'formula_term', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.requires.setdefault('formula_terms', {})[context.lookup_data('term')] = context.lookup_data('var_name')
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_rules_cf')
  
  fc_rule.fc_rule('fc_default', This_rule_base, fc_default,
    (),
    ())
  
  fc_rule.fc_rule('fc_provides_grid_mapping_rotated_latitude_longitude', This_rule_base, fc_provides_grid_mapping_rotated_latitude_longitude,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('rotated_latitude_longitude'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_latitude_longitude', This_rule_base, fc_provides_grid_mapping_latitude_longitude,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('latitude_longitude'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_transverse_mercator', This_rule_base, fc_provides_grid_mapping_transverse_mercator,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('transverse_mercator'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_mercator', This_rule_base, fc_provides_grid_mapping_mercator,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('mercator'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_stereographic', This_rule_base, fc_provides_grid_mapping_stereographic,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('stereographic'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_lambert_conformal', This_rule_base, fc_provides_grid_mapping_lambert_conformal,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('lambert_conformal'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_lambert_azimuthal_equal_area', This_rule_base, fc_provides_grid_mapping_lambert_azimuthal_equal_area,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('lambert_azimuthal_equal_area'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_albers_equal_area', This_rule_base, fc_provides_grid_mapping_albers_equal_area,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('albers_equal_area'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_vertical_perspective', This_rule_base, fc_provides_grid_mapping_vertical_perspective,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('vertical_perspective'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_geostationary', This_rule_base, fc_provides_grid_mapping_geostationary,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('geostationary'),))
  
  fc_rule.fc_rule('fc_provides_coordinate_latitude', This_rule_base, fc_provides_coordinate_latitude,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('latitude'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_provides_coordinate_longitude', This_rule_base, fc_provides_coordinate_longitude,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('longitude'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_provides_projection_x_coordinate', This_rule_base, fc_provides_projection_x_coordinate,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('projection_x_coordinate'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_provides_projection_y_coordinate', This_rule_base, fc_provides_projection_y_coordinate,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('projection_y_coordinate'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_provides_coordinate_time', This_rule_base, fc_provides_coordinate_time,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('time'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_provides_coordinate_time_period', This_rule_base, fc_provides_coordinate_time_period,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('time_period'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_build_label_coordinate', This_rule_base, fc_build_label_coordinate,
    (('facts_cf', 'label',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_time', This_rule_base, fc_build_auxiliary_coordinate_time,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_time_period', This_rule_base, fc_build_auxiliary_coordinate_time_period,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_latitude', This_rule_base, fc_build_auxiliary_coordinate_latitude,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_latitude_rotated', This_rule_base, fc_build_auxiliary_coordinate_latitude_rotated,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_longitude', This_rule_base, fc_build_auxiliary_coordinate_longitude,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_longitude_rotated', This_rule_base, fc_build_auxiliary_coordinate_longitude_rotated,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate', This_rule_base, fc_build_auxiliary_coordinate,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_cell_measure', This_rule_base, fc_build_cell_measure,
    (('facts_cf', 'cell_measure',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_latitude', This_rule_base, fc_build_coordinate_latitude,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('latitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('latitude_longitude'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_latitude_rotated', This_rule_base, fc_build_coordinate_latitude_rotated,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('latitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('rotated_latitude_longitude'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_longitude', This_rule_base, fc_build_coordinate_longitude,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('longitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('latitude_longitude'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_longitude_rotated', This_rule_base, fc_build_coordinate_longitude_rotated,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('longitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('rotated_latitude_longitude'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_latitude_nocs', This_rule_base, fc_build_coordinate_latitude_nocs,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('latitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('latitude_longitude'),),
      True),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('rotated_latitude_longitude'),),
      True),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_longitude_nocs', This_rule_base, fc_build_coordinate_longitude_nocs,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('longitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('latitude_longitude'),),
      True),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('rotated_latitude_longitude'),),
      True),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_transverse_mercator', This_rule_base, fc_build_coordinate_projection_x_transverse_mercator,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('transverse_mercator'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_transverse_mercator', This_rule_base, fc_build_coordinate_projection_y_transverse_mercator,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('transverse_mercator'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_lambert_conformal', This_rule_base, fc_build_coordinate_projection_x_lambert_conformal,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('lambert_conformal'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_lambert_conformal', This_rule_base, fc_build_coordinate_projection_y_lambert_conformal,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('lambert_conformal'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_mercator', This_rule_base, fc_build_coordinate_projection_x_mercator,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('mercator'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_mercator', This_rule_base, fc_build_coordinate_projection_y_mercator,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('mercator'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_stereographic', This_rule_base, fc_build_coordinate_projection_x_stereographic,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('stereographic'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_stereographic', This_rule_base, fc_build_coordinate_projection_y_stereographic,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('stereographic'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_lambert_azimuthal_equal_area', This_rule_base, fc_build_coordinate_projection_x_lambert_azimuthal_equal_area,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('lambert_azimuthal_equal_area'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_lambert_azimuthal_equal_area', This_rule_base, fc_build_coordinate_projection_y_lambert_azimuthal_equal_area,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('lambert_azimuthal_equal_area'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_albers_equal_area', This_rule_base, fc_build_coordinate_projection_x_albers_equal_area,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('albers_equal_area'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_albers_equal_area', This_rule_base, fc_build_coordinate_projection_y_albers_equal_area,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('albers_equal_area'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_vertical_perspective', This_rule_base, fc_build_coordinate_projection_x_vertical_perspective,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('vertical_perspective'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_vertical_perspective', This_rule_base, fc_build_coordinate_projection_y_vertical_perspective,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('vertical_perspective'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_geostationary', This_rule_base, fc_build_coordinate_projection_x_geostationary,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('geostationary'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_geostationary', This_rule_base, fc_build_coordinate_projection_y_geostationary,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('geostationary'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_time', This_rule_base, fc_build_coordinate_time,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('time'),
       contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_time_period', This_rule_base, fc_build_coordinate_time_period,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('time_period'),
       contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_default_coordinate', This_rule_base, fc_default_coordinate,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       contexts.anonymous('_'),
       contexts.variable('coordinate'),),
      True),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('miscellaneous'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_attribute_ukmo__um_stash_source', This_rule_base, fc_attribute_ukmo__um_stash_source,
    (),
    ())
  
  fc_rule.fc_rule('fc_attribute_ukmo__process_flags', This_rule_base, fc_attribute_ukmo__process_flags,
    (),
    ())
  
  fc_rule.fc_rule('fc_formula_type_atmosphere_hybrid_height_coordinate', This_rule_base, fc_formula_type_atmosphere_hybrid_height_coordinate,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('atmosphere_hybrid_height_coordinate'),))
  
  fc_rule.fc_rule('fc_formula_type_atmosphere_hybrid_sigma_pressure_coordinate', This_rule_base, fc_formula_type_atmosphere_hybrid_sigma_pressure_coordinate,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('atmosphere_hybrid_height_coordinate'),))
  
  fc_rule.fc_rule('fc_formula_type_ocean_sigma_z_coordinate', This_rule_base, fc_formula_type_ocean_sigma_z_coordinate,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('ocean_sigma_z_coordinate'),))
  
  fc_rule.fc_rule('fc_formula_type_ocean_sigma_coordinate', This_rule_base, fc_formula_type_ocean_sigma_coordinate,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('ocean_sigma_coordinate'),))
  
  fc_rule.fc_rule('fc_formula_type_ocean_s_coordinate', This_rule_base, fc_formula_type_ocean_s_coordinate,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('ocean_s_coordinate'),))
  
  fc_rule.fc_rule('fc_formula_type_ocean_s_coordinate_g1', This_rule_base, fc_formula_type_ocean_s_coordinate_g1,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('ocean_s_coordinate_g1'),))
  
  fc_rule.fc_rule('fc_formula_type_ocean_s_coordinate_g2', This_rule_base, fc_formula_type_ocean_s_coordinate_g2,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('ocean_s_coordinate_g2'),))
  
  fc_rule.fc_rule('fc_formula_terms', This_rule_base, fc_formula_terms,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'formula_term',
      (contexts.variable('var_name'),
       contexts.variable('coordinate'),
       contexts.variable('term'),),
      False),),
    ())

import six
import warnings
import cf_units
import netCDF4
import numpy as np
import numpy.ma as ma
import iris.aux_factory
import iris.coords
import iris.coord_systems
import iris.fileformats.cf as cf
import iris.fileformats.netcdf
from iris.fileformats.netcdf import _get_cf_var_data, parse_cell_methods, UnknownCellMethodWarning
import iris.fileformats.pp as pp
import iris.exceptions
import iris.std_names
import iris.util
from iris._cube_coord_common import get_valid_standard_name
from iris._lazy_data import as_lazy_data
UD_UNITS_LAT = ['degrees_north', 'degree_north', 'degree_n', 'degrees_n',
                'degreen', 'degreesn', 'degrees', 'degrees north',
                'degree north', 'degree n', 'degrees n']
UD_UNITS_LON = ['degrees_east', 'degree_east', 'degree_e', 'degrees_e',
                'degreee', 'degreese', 'degrees', 'degrees east',
                'degree east', 'degree e', 'degrees e']
CF_COORD_VERTICAL = {'atmosphere_ln_pressure_coordinate':['p0', 'lev'],
                     'atmosphere_sigma_coordinate':['sigma', 'ps', 'ptop'],
                     'atmosphere_hybrid_sigma_pressure_coordinate':['a', 'b', 'ps', 'p0'],
                     'atmosphere_hybrid_height_coordinate':['a', 'b', 'orog'],
                     'atmosphere_sleve_coordinate':['a', 'b1', 'b2', 'ztop', 'zsurf1', 'zsurf2'],
                     'ocean_sigma_coordinate':['sigma', 'eta', 'depth'],
                     'ocean_s_coordinate':['s', 'eta', 'depth', 'a', 'b', 'depth_c'],
                     'ocean_sigma_z_coordinate':['sigma', 'eta', 'depth', 'depth_c', 'nsigma', 'zlev'],
                     'ocean_double_sigma_coordinate':['sigma', 'depth', 'z1', 'z2', 'a', 'href', 'k_c'],
                     'ocean_s_coordinate_g1':['s', 'eta', 'depth', 'depth_c', 'C'],
                     'ocean_s_coordinate_g2':['s', 'eta', 'depth', 'depth_c', 'C']}
CF_GRID_MAPPING_ALBERS = 'albers_conical_equal_area'
CF_GRID_MAPPING_AZIMUTHAL = 'azimuthal_equidistant'
CF_GRID_MAPPING_LAMBERT_AZIMUTHAL = 'lambert_azimuthal_equal_area'
CF_GRID_MAPPING_LAMBERT_CONFORMAL = 'lambert_conformal_conic'
CF_GRID_MAPPING_LAMBERT_CYLINDRICAL = 'lambert_cylindrical_equal_area'
CF_GRID_MAPPING_LAT_LON = 'latitude_longitude'
CF_GRID_MAPPING_MERCATOR = 'mercator'
CF_GRID_MAPPING_ORTHO = 'orthographic'
CF_GRID_MAPPING_POLAR = 'polar_stereographic'
CF_GRID_MAPPING_ROTATED_LAT_LON = 'rotated_latitude_longitude'
CF_GRID_MAPPING_STEREO = 'stereographic'
CF_GRID_MAPPING_TRANSVERSE = 'transverse_mercator'
CF_GRID_MAPPING_VERTICAL = 'vertical_perspective'
CF_GRID_MAPPING_GEOSTATIONARY = 'geostationary'
CF_ATTR_AXIS = 'axis'
CF_ATTR_BOUNDS = 'bounds'
CF_ATTR_CALENDAR = 'calendar'
CF_ATTR_CLIMATOLOGY = 'climatology'
CF_ATTR_GRID_INVERSE_FLATTENING = 'inverse_flattening'
CF_ATTR_GRID_EARTH_RADIUS = 'earth_radius'
CF_ATTR_GRID_MAPPING_NAME = 'grid_mapping_name'
CF_ATTR_GRID_NORTH_POLE_LAT = 'grid_north_pole_latitude'
CF_ATTR_GRID_NORTH_POLE_LON = 'grid_north_pole_longitude'
CF_ATTR_GRID_NORTH_POLE_GRID_LON = 'north_pole_grid_longitude'
CF_ATTR_GRID_SEMI_MAJOR_AXIS = 'semi_major_axis'
CF_ATTR_GRID_SEMI_MINOR_AXIS = 'semi_minor_axis'
CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN = 'latitude_of_projection_origin'
CF_ATTR_GRID_LON_OF_PROJ_ORIGIN = 'longitude_of_projection_origin'
CF_ATTR_GRID_STANDARD_PARALLEL = 'standard_parallel'
CF_ATTR_GRID_FALSE_EASTING = 'false_easting'
CF_ATTR_GRID_FALSE_NORTHING = 'false_northing'
CF_ATTR_GRID_SCALE_FACTOR_AT_PROJ_ORIGIN = 'scale_factor_at_projection_origin'
CF_ATTR_GRID_SCALE_FACTOR_AT_CENT_MERIDIAN = 'scale_factor_at_central_meridian'
CF_ATTR_GRID_LON_OF_CENT_MERIDIAN = 'longitude_of_central_meridian'
CF_ATTR_GRID_STANDARD_PARALLEL = 'standard_parallel'
CF_ATTR_GRID_PERSPECTIVE_HEIGHT = 'perspective_point_height'
CF_ATTR_GRID_SWEEP_ANGLE_AXIS = 'sweep_angle_axis'
CF_ATTR_POSITIVE = 'positive'
CF_ATTR_STD_NAME = 'standard_name'
CF_ATTR_LONG_NAME = 'long_name'
CF_ATTR_UNITS = 'units'
CF_ATTR_CELL_METHODS = 'cell_methods'
CF_VALUE_AXIS_X = 'x'
CF_VALUE_AXIS_Y = 'y'
CF_VALUE_AXIS_T = 't'
CF_VALUE_AXIS_Z = 'z'
CF_VALUE_POSITIVE = ['down', 'up']
CF_VALUE_STD_NAME_LAT = 'latitude'
CF_VALUE_STD_NAME_LON = 'longitude'
CF_VALUE_STD_NAME_GRID_LAT = 'grid_latitude'
CF_VALUE_STD_NAME_GRID_LON = 'grid_longitude'
CF_VALUE_STD_NAME_PROJ_X = 'projection_x_coordinate'
CF_VALUE_STD_NAME_PROJ_Y = 'projection_y_coordinate'
def build_cube_metadata(engine):
    """Add the standard meta data to the cube."""
    cf_var = engine.cf_var
    cube = engine.cube
    cube.var_name = cf_var.cf_name
    standard_name = getattr(cf_var, CF_ATTR_STD_NAME, None)
    long_name = getattr(cf_var, CF_ATTR_LONG_NAME, None)
    cube.long_name = long_name
    if standard_name is not None:
        try:
            cube.standard_name = get_valid_standard_name(standard_name)
        except ValueError:
            if cube.long_name is not None:
                cube.attributes['invalid_standard_name'] = standard_name
            else:
                cube.long_name = standard_name
    attr_units = get_attr_units(cf_var, cube.attributes)
    cube.units = attr_units
    nc_att_cell_methods = getattr(cf_var, CF_ATTR_CELL_METHODS, None)
    with warnings.catch_warnings(record=True) as warning_records:
        cube.cell_methods = parse_cell_methods(nc_att_cell_methods)
    warning_records = [record for record in warning_records
                       if issubclass(record.category, UnknownCellMethodWarning)]
    if len(warning_records) > 0:
        warn_record = warning_records[0]
        name = '{}'.format(cf_var.cf_name)
        msg = warn_record.message.args[0]
        msg = msg.replace('variable', 'variable {!r}'.format(name))
        warnings.warn(message=msg, category=UnknownCellMethodWarning)
    for attr_name, attr_value in six.iteritems(cf_var.cf_group.global_attributes):
        try:
            if six.PY2 and isinstance(attr_value, six.text_type):
                try:
                    cube.attributes[str(attr_name)] = str(attr_value)
                except UnicodeEncodeError:
                    cube.attributes[str(attr_name)] = attr_value
            else:
                cube.attributes[str(attr_name)] = attr_value
        except ValueError as e:
            msg = 'Skipping global attribute {!r}: {}'
            warnings.warn(msg.format(attr_name, str(e)))
def _get_ellipsoid(cf_grid_var):
    """Return the ellipsoid definition."""
    major = getattr(cf_grid_var, CF_ATTR_GRID_SEMI_MAJOR_AXIS, None)
    minor = getattr(cf_grid_var, CF_ATTR_GRID_SEMI_MINOR_AXIS, None)
    inverse_flattening = getattr(cf_grid_var, CF_ATTR_GRID_INVERSE_FLATTENING, None)
    if major is not None and minor is not None:
        inverse_flattening = None
    if major is None and minor is None and inverse_flattening is None:
        major = getattr(cf_grid_var, CF_ATTR_GRID_EARTH_RADIUS, None)
    return major, minor, inverse_flattening
def build_coordinate_system(cf_grid_var):
    """Create a coordinate system from the CF-netCDF grid mapping variable."""
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    return iris.coord_systems.GeogCS(major, minor, inverse_flattening)
def build_rotated_coordinate_system(engine, cf_grid_var):
    """Create a rotated coordinate system from the CF-netCDF grid mapping variable."""
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    north_pole_latitude = getattr(cf_grid_var, CF_ATTR_GRID_NORTH_POLE_LAT, 90.0)
    north_pole_longitude = getattr(cf_grid_var, CF_ATTR_GRID_NORTH_POLE_LON, 0.0)
    if north_pole_latitude is None or north_pole_longitude is None:
        warnings.warn('Rotated pole position is not fully specified')
    north_pole_grid_lon = getattr(cf_grid_var, CF_ATTR_GRID_NORTH_POLE_GRID_LON, 0.0)
    ellipsoid = None
    if major is not None or minor is not None or inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor, inverse_flattening)
    rcs = iris.coord_systems.RotatedGeogCS(north_pole_latitude, north_pole_longitude,
                                           north_pole_grid_lon, ellipsoid)
    return rcs
def build_transverse_mercator_coordinate_system(engine, cf_grid_var):
    """
        Create a transverse Mercator coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_central_meridian = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_CENT_MERIDIAN, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    scale_factor_at_central_meridian = getattr(
        cf_grid_var, CF_ATTR_GRID_SCALE_FACTOR_AT_CENT_MERIDIAN, None)
    if longitude_of_central_meridian is None:
        longitude_of_central_meridian = getattr(
            cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    if scale_factor_at_central_meridian is None:
        scale_factor_at_central_meridian = getattr(
            cf_grid_var, CF_ATTR_GRID_SCALE_FACTOR_AT_PROJ_ORIGIN, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.TransverseMercator(
        latitude_of_projection_origin, longitude_of_central_meridian,
        false_easting, false_northing, scale_factor_at_central_meridian,
        ellipsoid)
    return cs
def build_lambert_conformal_coordinate_system(engine, cf_grid_var):
    """
        Create a Lambert conformal conic coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_central_meridian = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_CENT_MERIDIAN, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    standard_parallel = getattr(
        cf_grid_var, CF_ATTR_GRID_STANDARD_PARALLEL, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.LambertConformal(
        latitude_of_projection_origin, longitude_of_central_meridian,
        false_easting, false_northing, standard_parallel,
        ellipsoid)
    return cs
def build_stereographic_coordinate_system(engine, cf_grid_var):
    """
        Create a stereographic coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.Stereographic(
        latitude_of_projection_origin, longitude_of_projection_origin,
        false_easting, false_northing,
        true_scale_lat=None,
        ellipsoid=ellipsoid)
    return cs
def build_mercator_coordinate_system(engine, cf_grid_var):
    """
        Create a Mercator coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    longitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.Mercator(
        longitude_of_projection_origin,
        ellipsoid=ellipsoid)
    return cs
def build_lambert_azimuthal_equal_area_coordinate_system(engine, cf_grid_var):
    """
        Create a lambert azimuthal equal area coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.LambertAzimuthalEqualArea(
        latitude_of_projection_origin, longitude_of_projection_origin,
        false_easting, false_northing, ellipsoid)
    return cs
def build_albers_equal_area_coordinate_system(engine, cf_grid_var):
    """
        Create a albers conical equal area coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_central_meridian = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_CENT_MERIDIAN, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    standard_parallels = getattr(
        cf_grid_var, CF_ATTR_GRID_STANDARD_PARALLEL, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.AlbersEqualArea(
        latitude_of_projection_origin, longitude_of_central_meridian,
        false_easting, false_northing, standard_parallels, ellipsoid)
    return cs
def build_vertical_perspective_coordinate_system(engine, cf_grid_var):
    """
        Create a vertical perspective coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    perspective_point_height = getattr(
        cf_grid_var, CF_ATTR_GRID_PERSPECTIVE_HEIGHT, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.VerticalPerspective(
        latitude_of_projection_origin, longitude_of_projection_origin,
        perspective_point_height, false_easting, false_northing, ellipsoid)
    return cs
def build_geostationary_coordinate_system(engine, cf_grid_var):
    """
        Create a geostationary coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    perspective_point_height = getattr(
        cf_grid_var, CF_ATTR_GRID_PERSPECTIVE_HEIGHT, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    sweep_angle_axis = getattr(
        cf_grid_var, CF_ATTR_GRID_SWEEP_ANGLE_AXIS, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.Geostationary(
        latitude_of_projection_origin, longitude_of_projection_origin,
        perspective_point_height, sweep_angle_axis, false_easting,
        false_northing, ellipsoid)
    return cs
def get_attr_units(cf_var, attributes):
    attr_units = getattr(cf_var, CF_ATTR_UNITS, cf_units._UNIT_DIMENSIONLESS)
    if not attr_units:
        attr_units = '1'
    if attr_units in UD_UNITS_LAT or attr_units in UD_UNITS_LON:
        attr_units = 'degrees'
    try:
        cf_units.as_unit(attr_units)
    except ValueError:
        msg = u'Ignoring netCDF variable {!r} invalid units {!r}'.format(
            cf_var.cf_name, attr_units)
        if six.PY3:
            warnings.warn(msg)
        else:
            warnings.warn(msg.encode('ascii', errors='backslashreplace'))
        attributes['invalid_units'] = attr_units
        attr_units = cf_units._UNKNOWN_UNIT_STRING
    if np.issubdtype(cf_var.dtype, np.str_):
        attr_units = cf_units._NO_UNIT_STRING
    if cf_units.as_unit(attr_units).is_time_reference():
        attr_calendar = getattr(cf_var, CF_ATTR_CALENDAR, None)
        if attr_calendar:
            attr_units = cf_units.Unit(attr_units, calendar=attr_calendar)
    return attr_units
def get_names(cf_coord_var, coord_name, attributes):
    """Determine the standard_name, long_name and var_name attributes."""
    standard_name = getattr(cf_coord_var, CF_ATTR_STD_NAME, None)
    long_name = getattr(cf_coord_var, CF_ATTR_LONG_NAME, None)
    cf_name = str(cf_coord_var.cf_name)
    if standard_name is not None:
        try:
            standard_name = get_valid_standard_name(standard_name)
        except ValueError:
            if long_name is not None:
                attributes['invalid_standard_name'] = standard_name
                if coord_name is not None:
                    standard_name = coord_name
                else:
                    standard_name = None
            else:
                if coord_name is not None:
                    attributes['invalid_standard_name'] = standard_name
                    standard_name = coord_name
                else:
                    standard_name = None
    else:
        if coord_name is not None:
            standard_name = coord_name
    if standard_name is None:
        if cf_name in iris.std_names.STD_NAMES:
            standard_name = cf_name
    return (standard_name, long_name, cf_name)
def get_cf_bounds_var(cf_coord_var):
    """
        Return the CF variable representing the bounds of a coordinate
        variable.

        """
    attr_bounds = getattr(cf_coord_var, CF_ATTR_BOUNDS, None)
    attr_climatology = getattr(cf_coord_var, CF_ATTR_CLIMATOLOGY, None)
    cf_bounds_var = None
    climatological = False
    if attr_bounds is not None:
        bounds_vars = cf_coord_var.cf_group.bounds
        if attr_bounds in bounds_vars:
            cf_bounds_var = bounds_vars[attr_bounds]
    elif attr_climatology is not None:
        climatology_vars = cf_coord_var.cf_group.climatology
        if attr_climatology in climatology_vars:
            cf_bounds_var = climatology_vars[attr_climatology]
            climatological = True
    if attr_bounds is not None and attr_climatology is not None:
        warnings.warn('Ignoring climatology in favour of bounds attribute '
                      'on NetCDF variable {!r}.'.format(
                      cf_coord_var.cf_name))
    return cf_bounds_var, climatological
def reorder_bounds_data(bounds_data, cf_bounds_var, cf_coord_var):
    """
        Return a bounds_data array with the vertex dimension as the most
        rapidly varying.

        .. note::

            This function assumes the dimension names of the coordinate
            variable match those of the bounds variable in order to determine
            which is the vertex dimension.


        """
    vertex_dim_names = set(cf_bounds_var.dimensions).difference(
        cf_coord_var.dimensions)
    if len(vertex_dim_names) != 1:
        msg = 'Too many dimension names differ between coordinate ' \
                  'variable {!r} and the bounds variable {!r}. ' \
                  'Expected 1, got {}.'
        raise ValueError(msg.format(str(cf_coord_var.cf_name),
                                    str(cf_bounds_var.cf_name),
                                    len(vertex_dim_names)))
    vertex_dim = cf_bounds_var.dimensions.index(*vertex_dim_names)
    bounds_data = np.rollaxis(bounds_data.view(), vertex_dim,
                              len(bounds_data.shape))
    return bounds_data
def build_dimension_coordinate(engine, cf_coord_var, coord_name=None, coord_system=None):
    """Create a dimension coordinate (DimCoord) and add it to the cube."""
    cf_var = engine.cf_var
    cube = engine.cube
    attributes = {}
    attr_units = get_attr_units(cf_coord_var, attributes)
    points_data = cf_coord_var[:]
    if ma.is_masked(points_data):
        points_data = ma.filled(points_data)
        msg = 'Gracefully filling {!r} dimension coordinate masked points'
        warnings.warn(msg.format(str(cf_coord_var.cf_name)))
    cf_bounds_var, climatological = get_cf_bounds_var(
        cf_coord_var)
    if cf_bounds_var is not None:
        bounds_data = cf_bounds_var[:]
        if ma.is_masked(bounds_data):
            bounds_data = ma.filled(bounds_data)
            msg = 'Gracefully filling {!r} dimension coordinate masked bounds'
            warnings.warn(msg.format(str(cf_coord_var.cf_name)))
        if cf_bounds_var.shape[:-1] != cf_coord_var.shape:
            bounds_data = reorder_bounds_data(bounds_data, cf_bounds_var,
                                              cf_coord_var)
    else:
        bounds_data = None
    circular = False
    if points_data.ndim == 1 and coord_name in [CF_VALUE_STD_NAME_LON, CF_VALUE_STD_NAME_GRID_LON] \
            and cf_units.Unit(attr_units) in [cf_units.Unit('radians'), cf_units.Unit('degrees')]:
            modulus_value = cf_units.Unit(attr_units).modulus
            circular = iris.util._is_circular(points_data, modulus_value, bounds=bounds_data)
    common_dims = [dim for dim in cf_coord_var.dimensions
                   if dim in cf_var.dimensions]
    data_dims = None
    if common_dims:
        data_dims = [cf_var.dimensions.index(dim) for dim in common_dims]
    standard_name, long_name, var_name = get_names(cf_coord_var, coord_name, attributes)
    try:
        coord = iris.coords.DimCoord(points_data,
                                     standard_name=standard_name,
                                     long_name=long_name,
                                     var_name=var_name,
                                     units=attr_units,
                                     bounds=bounds_data,
                                     attributes=attributes,
                                     coord_system=coord_system,
                                     circular=circular,
                                     climatological=
                                         climatological)
    except ValueError as e_msg:
        coord = iris.coords.AuxCoord(points_data,
                                     standard_name=standard_name,
                                     long_name=long_name,
                                     var_name=var_name,
                                     units=attr_units,
                                     bounds=bounds_data,
                                     attributes=attributes,
                                     coord_system=coord_system,
                                     climatological=
                                         climatological)
        cube.add_aux_coord(coord, data_dims)
        msg = 'Failed to create {name!r} dimension coordinate: {error}\n' \
                  'Gracefully creating {name!r} auxiliary coordinate instead.'
        warnings.warn(msg.format(name=str(cf_coord_var.cf_name),
                                 error=e_msg))
    else:
        if data_dims:
            cube.add_dim_coord(coord, data_dims)
        else:
            cube.add_aux_coord(coord, data_dims)
    engine.provides['coordinates'].append((coord, cf_coord_var.cf_name))
def build_auxiliary_coordinate(engine, cf_coord_var, coord_name=None, coord_system=None):
    """Create an auxiliary coordinate (AuxCoord) and add it to the cube."""
    cf_var = engine.cf_var
    cube = engine.cube
    attributes = {}
    attr_units = get_attr_units(cf_coord_var, attributes)
    if isinstance(cf_coord_var, cf.CFLabelVariable):
        points_data = cf_coord_var.cf_label_data(cf_var)
    else:
        points_data = _get_cf_var_data(cf_coord_var, engine.filename)
    cf_bounds_var, climatological = get_cf_bounds_var(
        cf_coord_var)
    if cf_bounds_var is not None:
        bounds_data = _get_cf_var_data(cf_bounds_var, engine.filename)
        if cf_bounds_var.shape[:-1] != cf_coord_var.shape:
            bounds_data = np.asarray(bounds_data)
            bounds_data = reorder_bounds_data(bounds_data, cf_bounds_var,
                                              cf_coord_var)
    else:
        bounds_data = None
    common_dims = [dim for dim in cf_coord_var.dimensions
                   if dim in cf_var.dimensions]
    data_dims = None
    if common_dims:
        data_dims = [cf_var.dimensions.index(dim) for dim in common_dims]
    standard_name, long_name, var_name = get_names(cf_coord_var, coord_name, attributes)
    coord = iris.coords.AuxCoord(points_data,
                                 standard_name=standard_name,
                                 long_name=long_name,
                                 var_name=var_name,
                                 units=attr_units,
                                 bounds=bounds_data,
                                 attributes=attributes,
                                 coord_system=coord_system,
                                 climatological=
                                     climatological)
    cube.add_aux_coord(coord, data_dims)
    engine.provides['coordinates'].append((coord, cf_coord_var.cf_name))
def build_cell_measures(engine, cf_cm_attr, coord_name=None):
    """Create a CellMeasure instance and add it to the cube."""
    cf_var = engine.cf_var
    cube = engine.cube
    attributes = {}
    attr_units = get_attr_units(cf_cm_attr, attributes)
    data = _get_cf_var_data(cf_cm_attr, engine.filename)
    common_dims = [dim for dim in cf_cm_attr.dimensions
                   if dim in cf_var.dimensions]
    data_dims = None
    if common_dims:
        data_dims = [cf_var.dimensions.index(dim) for dim in common_dims]
    standard_name, long_name, var_name = get_names(cf_cm_attr, coord_name, attributes)
    measure = cf_cm_attr.cf_measure
    cell_measure = iris.coords.CellMeasure(data,
                                           standard_name=standard_name,
                                           long_name=long_name,
                                           var_name=var_name,
                                           units=attr_units,
                                           attributes=attributes,
                                           measure=measure)
    cube.add_cell_measure(cell_measure, data_dims)
def _is_lat_lon(cf_var, ud_units, std_name, std_name_grid, axis_name, prefixes):
    """
        Determine whether the CF coordinate variable is a latitude/longitude variable.

        Ref: [CF] Section 4.1 Latitude Coordinate.
             [CF] Section 4.2 Longitude Coordinate.

        """
    is_valid = False
    attr_units = getattr(cf_var, CF_ATTR_UNITS, None)
    if attr_units is not None:
        attr_units = attr_units.lower()
        is_valid = attr_units in ud_units
        if attr_units == 'degrees':
            attr_std_name = getattr(cf_var, CF_ATTR_STD_NAME, None)
            if attr_std_name is not None:
                is_valid = attr_std_name.lower() == std_name_grid
            else:
                is_valid = False
                attr_axis = getattr(cf_var, CF_ATTR_AXIS, None)
                if attr_axis is not None:
                    is_valid = attr_axis.lower() == axis_name
    else:
        attr_std_name = getattr(cf_var, CF_ATTR_STD_NAME, None)
        if attr_std_name is not None:
            attr_std_name = attr_std_name.lower()
            is_valid = attr_std_name in [std_name, std_name_grid]
            if not is_valid:
                is_valid = any([attr_std_name.startswith(prefix) for prefix in prefixes])
        else:
            attr_axis = getattr(cf_var, CF_ATTR_AXIS, None)
            if attr_axis is not None:
                is_valid = attr_axis.lower() == axis_name
    return is_valid
def is_latitude(engine, cf_name):
    """Determine whether the CF coordinate variable is a latitude variable."""
    cf_var = engine.cf_var.cf_group[cf_name]
    return _is_lat_lon(cf_var, UD_UNITS_LAT, CF_VALUE_STD_NAME_LAT,
                       CF_VALUE_STD_NAME_GRID_LAT, CF_VALUE_AXIS_Y, ['lat', 'rlat'])
def is_longitude(engine, cf_name):
    """Determine whether the CF coordinate variable is a longitude variable."""
    cf_var = engine.cf_var.cf_group[cf_name]
    return _is_lat_lon(cf_var, UD_UNITS_LON, CF_VALUE_STD_NAME_LON,
                       CF_VALUE_STD_NAME_GRID_LON, CF_VALUE_AXIS_X, ['lon', 'rlon'])
def is_projection_x_coordinate(engine, cf_name):
    """
        Determine whether the CF coordinate variable is a
        projection_x_coordinate variable.

        """
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_name = getattr(cf_var, CF_ATTR_STD_NAME, None) or \
            getattr(cf_var, CF_ATTR_LONG_NAME, None)
    return attr_name == CF_VALUE_STD_NAME_PROJ_X
def is_projection_y_coordinate(engine, cf_name):
    """
        Determine whether the CF coordinate variable is a
        projection_y_coordinate variable.

        """
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_name = getattr(cf_var, CF_ATTR_STD_NAME, None) or \
            getattr(cf_var, CF_ATTR_LONG_NAME, None)
    return attr_name == CF_VALUE_STD_NAME_PROJ_Y
def is_time(engine, cf_name):
    """
        Determine whether the CF coordinate variable is a time variable.

        Ref: [CF] Section 4.4 Time Coordinate.

        """
    is_valid = False
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_units = getattr(cf_var, CF_ATTR_UNITS, None)
    attr_std_name = getattr(cf_var, CF_ATTR_STD_NAME, None)
    attr_axis = getattr(cf_var, CF_ATTR_AXIS, '')
    try:
        is_time_reference = cf_units.Unit(attr_units or 1).is_time_reference()
    except ValueError:
        is_time_reference = False
    return is_time_reference and (attr_std_name=='time' or attr_axis.lower()==CF_VALUE_AXIS_T)
def is_time_period(engine, cf_name):
    """Determine whether the CF coordinate variable represents a time period."""
    is_valid = False
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_units = getattr(cf_var, CF_ATTR_UNITS, None)
    if attr_units is not None:
        try:
            is_valid = cf_units.is_time(attr_units)
        except ValueError:
            is_valid = False
    return is_valid
def is_grid_mapping(engine, cf_name, grid_mapping):
    """Determine whether the CF grid mapping variable is of the appropriate type."""
    is_valid = False
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_mapping_name = getattr(cf_var, CF_ATTR_GRID_MAPPING_NAME, None)
    if attr_mapping_name is not None:
        is_valid = attr_mapping_name.lower() == grid_mapping
    return is_valid
def _is_rotated(engine, cf_name, cf_attr_value):
    """Determine whether the CF coordinate variable is rotated."""
    is_valid = False
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_std_name = getattr(cf_var, CF_ATTR_STD_NAME, None)
    if attr_std_name is not None:
        is_valid = attr_std_name.lower() == cf_attr_value
    else:
        attr_units = getattr(cf_var, CF_ATTR_UNITS, None)
        if attr_units is not None:
            is_valid = attr_units.lower() == 'degrees'
    return is_valid
def is_rotated_latitude(engine, cf_name):
    """Determine whether the CF coodinate variable is rotated latitude."""
    return _is_rotated(engine, cf_name, CF_VALUE_STD_NAME_GRID_LAT)
def is_rotated_longitude(engine, cf_name):
    """Determine whether the CF coordinate variable is rotated longitude."""
    return _is_rotated(engine, cf_name, CF_VALUE_STD_NAME_GRID_LON)
def has_supported_mercator_parameters(engine, cf_name):
    """Determine whether the CF grid mapping variable has the supported
        values for the parameters of the Mercator projection."""
    is_valid = True
    cf_grid_var = engine.cf_var.cf_group[cf_name]
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    scale_factor_at_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_SCALE_FACTOR_AT_PROJ_ORIGIN, None)
    standard_parallel = getattr(
        cf_grid_var, CF_ATTR_GRID_STANDARD_PARALLEL, None)
    if false_easting is not None and \
                false_easting != 0:
        warnings.warn('False eastings other than 0.0 not yet supported '
                      'for Mercator projections')
        is_valid = False
    if false_northing is not None and \
                false_northing != 0:
        warnings.warn('False northings other than 0.0 not yet supported '
                      'for Mercator projections')
        is_valid = False
    if scale_factor_at_projection_origin is not None and \
                scale_factor_at_projection_origin != 1:
        warnings.warn('Scale factors other than 1.0 not yet supported for '
                      'Mercator projections')
        is_valid = False
    if standard_parallel is not None and \
                standard_parallel != 0:
        warnings.warn('Standard parallels other than 0.0 not yet '
                      'supported for Mercator projections')
        is_valid = False
    return is_valid
def has_supported_stereographic_parameters(engine, cf_name):
    """Determine whether the CF grid mapping variable has a value of 1.0
        for the scale_factor_at_projection_origin attribute."""
    is_valid = True
    cf_grid_var = engine.cf_var.cf_group[cf_name]
    scale_factor_at_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_SCALE_FACTOR_AT_PROJ_ORIGIN, None)
    if scale_factor_at_projection_origin is not None and \
                scale_factor_at_projection_origin != 1:
        warnings.warn('Scale factors other than 1.0 not yet supported for '
                      'stereographic projections')
        is_valid = False
    return is_valid
def _parse_cell_methods(cf_var_name, nc_cell_methods):
    """Parse the CF cell_methods attribute string."""
    cell_methods = []
    if nc_cell_methods is not None:
        for m in CM_PARSE.finditer(nc_cell_methods):
            d = m.groupdict()
            method = d[CM_METHOD]
            method = method.strip()
            method_words = method.split()
            if method_words[0].lower() not in CM_KNOWN_METHODS:
                msg = 'NetCDF variable {!r} contains unknown cell ' \
                          'method {!r}'
                warnings.warn(msg.format('{}'.format(cf_var_name),
                                         '{}'.format(method_words[0])))
            d[CM_METHOD] = method
            name = d[CM_NAME]
            name = name.replace(' ', '')
            name = name.rstrip(':')
            d[CM_NAME] = tuple([n for n in name.split(':')])
            interval = []
            comment = []
            if d[CM_EXTRA] is not None:
                d[CM_EXTRA] = d[CM_EXTRA].replace('comment:', '<<comment>><<:>>')
                d[CM_EXTRA] = d[CM_EXTRA].replace('interval:', '<<interval>><<:>>')
                d[CM_EXTRA] = d[CM_EXTRA].split('<<:>>')
                if len(d[CM_EXTRA]) == 1:
                    comment.extend(d[CM_EXTRA])
                else:
                    next_field_type = comment
                    for field in d[CM_EXTRA]:
                        field_type = next_field_type
                        index = field.rfind('<<interval>>')
                        if index == 0:
                            next_field_type = interval
                            continue
                        elif index > 0:
                            next_field_type = interval
                        else:
                            index = field.rfind('<<comment>>')
                            if index == 0:
                                next_field_type = comment
                                continue
                            elif index > 0:
                                next_field_type = comment
                        if index != -1:
                            field = field[:index]
                        field_type.append(field.strip())
            if len(interval):
                if len(d[CM_NAME]) != len(interval) and len(interval) == 1:
                    interval = interval*len(d[CM_NAME])
            if len(comment):
                if len(d[CM_NAME]) != len(comment) and len(comment) == 1:
                    comment = comment*len(d[CM_NAME])
            d[CM_INTERVAL] = tuple(interval)
            d[CM_COMMENT] = tuple(comment)
            cell_methods.append(iris.coords.CellMethod(d[CM_METHOD], coords=d[CM_NAME], intervals=d[CM_INTERVAL], comments=d[CM_COMMENT]))
    return tuple(cell_methods)

Krb_filename = '../fc_rules_cf.krb'
Krb_lineno_map = (
    ((12, 12), (37, 37)),
    ((13, 13), (38, 38)),
    ((22, 26), (51, 51)),
    ((27, 27), (52, 52)),
    ((28, 28), (54, 54)),
    ((29, 29), (55, 55)),
    ((30, 30), (56, 56)),
    ((31, 33), (57, 57)),
    ((34, 34), (58, 58)),
    ((43, 47), (71, 71)),
    ((48, 48), (72, 72)),
    ((49, 49), (74, 74)),
    ((50, 50), (75, 75)),
    ((51, 51), (76, 76)),
    ((52, 54), (77, 77)),
    ((55, 55), (78, 78)),
    ((64, 68), (90, 90)),
    ((69, 69), (91, 91)),
    ((70, 70), (93, 93)),
    ((71, 71), (94, 94)),
    ((72, 72), (95, 95)),
    ((73, 75), (96, 96)),
    ((76, 76), (97, 97)),
    ((85, 89), (110, 110)),
    ((90, 90), (111, 111)),
    ((91, 91), (112, 112)),
    ((92, 92), (114, 114)),
    ((93, 93), (115, 115)),
    ((94, 94), (116, 116)),
    ((95, 97), (117, 117)),
    ((98, 98), (118, 118)),
    ((107, 111), (131, 131)),
    ((112, 112), (132, 132)),
    ((113, 113), (133, 133)),
    ((114, 114), (135, 135)),
    ((115, 115), (136, 136)),
    ((116, 116), (137, 137)),
    ((117, 119), (138, 138)),
    ((120, 120), (139, 139)),
    ((129, 133), (151, 151)),
    ((134, 134), (152, 152)),
    ((135, 135), (154, 154)),
    ((136, 136), (155, 155)),
    ((137, 137), (156, 156)),
    ((138, 140), (157, 157)),
    ((141, 141), (158, 158)),
    ((150, 154), (170, 170)),
    ((155, 155), (171, 171)),
    ((156, 156), (173, 173)),
    ((157, 157), (174, 174)),
    ((158, 158), (175, 175)),
    ((159, 161), (176, 176)),
    ((162, 162), (177, 177)),
    ((171, 175), (189, 189)),
    ((176, 176), (190, 190)),
    ((177, 177), (192, 192)),
    ((178, 178), (193, 193)),
    ((179, 179), (194, 194)),
    ((180, 182), (195, 195)),
    ((183, 183), (196, 196)),
    ((192, 196), (208, 208)),
    ((197, 197), (209, 209)),
    ((198, 198), (211, 211)),
    ((199, 200), (212, 213)),
    ((201, 201), (214, 214)),
    ((202, 204), (215, 215)),
    ((205, 205), (216, 216)),
    ((214, 218), (228, 228)),
    ((219, 220), (229, 230)),
    ((221, 221), (232, 232)),
    ((222, 223), (233, 234)),
    ((224, 224), (235, 235)),
    ((225, 227), (236, 236)),
    ((228, 228), (237, 237)),
    ((237, 241), (250, 250)),
    ((242, 242), (251, 251)),
    ((243, 246), (253, 253)),
    ((247, 247), (254, 254)),
    ((256, 260), (267, 267)),
    ((261, 261), (268, 268)),
    ((262, 265), (270, 270)),
    ((266, 266), (271, 271)),
    ((275, 279), (284, 284)),
    ((280, 280), (285, 285)),
    ((281, 284), (287, 287)),
    ((285, 285), (288, 288)),
    ((294, 298), (301, 301)),
    ((299, 299), (302, 302)),
    ((300, 303), (304, 304)),
    ((304, 304), (305, 305)),
    ((313, 317), (318, 318)),
    ((318, 318), (319, 319)),
    ((319, 322), (321, 321)),
    ((323, 323), (322, 322)),
    ((332, 336), (336, 336)),
    ((337, 337), (337, 337)),
    ((338, 341), (339, 339)),
    ((342, 342), (340, 340)),
    ((351, 355), (352, 352)),
    ((356, 356), (354, 354)),
    ((357, 357), (355, 355)),
    ((358, 358), (356, 356)),
    ((367, 371), (370, 370)),
    ((372, 372), (371, 371)),
    ((373, 373), (373, 373)),
    ((374, 374), (374, 374)),
    ((375, 375), (375, 375)),
    ((384, 388), (388, 388)),
    ((389, 389), (389, 389)),
    ((390, 390), (391, 391)),
    ((391, 391), (392, 392)),
    ((392, 392), (393, 393)),
    ((401, 405), (406, 406)),
    ((406, 406), (407, 407)),
    ((407, 407), (408, 408)),
    ((408, 408), (410, 410)),
    ((409, 410), (411, 412)),
    ((411, 411), (413, 413)),
    ((420, 424), (426, 426)),
    ((425, 425), (427, 427)),
    ((426, 426), (428, 428)),
    ((427, 427), (430, 430)),
    ((428, 429), (431, 432)),
    ((430, 430), (433, 433)),
    ((439, 443), (446, 446)),
    ((444, 444), (447, 447)),
    ((445, 445), (448, 448)),
    ((446, 446), (450, 450)),
    ((447, 448), (451, 452)),
    ((449, 449), (453, 453)),
    ((458, 462), (466, 466)),
    ((463, 463), (467, 467)),
    ((464, 464), (468, 468)),
    ((465, 465), (470, 470)),
    ((466, 467), (471, 472)),
    ((468, 468), (473, 473)),
    ((477, 481), (486, 486)),
    ((482, 482), (487, 487)),
    ((483, 483), (488, 488)),
    ((484, 484), (489, 489)),
    ((485, 485), (490, 490)),
    ((486, 486), (492, 492)),
    ((487, 487), (493, 493)),
    ((488, 488), (494, 494)),
    ((497, 501), (505, 505)),
    ((502, 502), (507, 507)),
    ((503, 503), (508, 508)),
    ((504, 504), (509, 509)),
    ((513, 517), (522, 522)),
    ((518, 522), (523, 523)),
    ((523, 523), (524, 524)),
    ((524, 524), (526, 526)),
    ((525, 527), (527, 529)),
    ((528, 528), (530, 530)),
    ((537, 541), (543, 543)),
    ((542, 546), (544, 544)),
    ((547, 547), (545, 545)),
    ((548, 548), (547, 547)),
    ((549, 551), (548, 550)),
    ((552, 552), (551, 551)),
    ((561, 565), (564, 564)),
    ((566, 570), (565, 565)),
    ((571, 571), (566, 566)),
    ((572, 572), (568, 568)),
    ((573, 575), (569, 571)),
    ((576, 576), (572, 572)),
    ((585, 589), (585, 585)),
    ((590, 594), (586, 586)),
    ((595, 595), (587, 587)),
    ((596, 596), (589, 589)),
    ((597, 599), (590, 592)),
    ((600, 600), (593, 593)),
    ((609, 613), (606, 606)),
    ((615, 618), (608, 608)),
    ((623, 626), (610, 610)),
    ((630, 630), (612, 612)),
    ((631, 633), (613, 615)),
    ((634, 634), (616, 616)),
    ((643, 647), (629, 629)),
    ((649, 652), (631, 631)),
    ((657, 660), (633, 633)),
    ((664, 664), (635, 635)),
    ((665, 667), (636, 638)),
    ((668, 668), (639, 639)),
    ((677, 681), (652, 652)),
    ((682, 686), (653, 653)),
    ((687, 687), (655, 655)),
    ((688, 690), (656, 658)),
    ((691, 691), (659, 659)),
    ((700, 704), (672, 672)),
    ((705, 709), (673, 673)),
    ((710, 710), (675, 675)),
    ((711, 713), (676, 678)),
    ((714, 714), (679, 679)),
    ((723, 727), (691, 691)),
    ((728, 732), (692, 692)),
    ((733, 733), (694, 694)),
    ((734, 736), (695, 697)),
    ((737, 737), (698, 698)),
    ((746, 750), (711, 711)),
    ((751, 755), (712, 712)),
    ((756, 756), (714, 714)),
    ((757, 759), (715, 717)),
    ((760, 760), (718, 718)),
    ((769, 773), (731, 731)),
    ((774, 778), (732, 732)),
    ((779, 779), (734, 734)),
    ((780, 782), (735, 737)),
    ((783, 783), (738, 738)),
    ((792, 796), (750, 750)),
    ((797, 801), (751, 751)),
    ((802, 802), (753, 753)),
    ((803, 805), (754, 756)),
    ((806, 806), (757, 757)),
    ((815, 819), (769, 769)),
    ((820, 824), (770, 770)),
    ((825, 825), (772, 772)),
    ((826, 828), (773, 775)),
    ((829, 829), (776, 776)),
    ((838, 842), (788, 788)),
    ((843, 847), (789, 789)),
    ((848, 848), (791, 791)),
    ((849, 851), (792, 794)),
    ((852, 852), (795, 795)),
    ((861, 865), (808, 808)),
    ((866, 870), (809, 809)),
    ((871, 871), (811, 811)),
    ((872, 874), (812, 814)),
    ((875, 875), (815, 815)),
    ((884, 888), (828, 828)),
    ((889, 893), (829, 829)),
    ((894, 894), (831, 831)),
    ((895, 897), (832, 834)),
    ((898, 898), (835, 835)),
    ((907, 911), (847, 847)),
    ((912, 916), (848, 848)),
    ((917, 917), (850, 850)),
    ((918, 920), (851, 853)),
    ((921, 921), (854, 854)),
    ((930, 934), (867, 867)),
    ((935, 939), (868, 868)),
    ((940, 940), (870, 870)),
    ((941, 943), (871, 873)),
    ((944, 944), (874, 874)),
    ((953, 957), (886, 886)),
    ((958, 962), (887, 887)),
    ((963, 963), (889, 889)),
    ((964, 966), (890, 892)),
    ((967, 967), (893, 893)),
    ((976, 980), (906, 906)),
    ((981, 985), (907, 907)),
    ((986, 986), (909, 909)),
    ((987, 989), (910, 912)),
    ((990, 990), (913, 913)),
    ((999, 1003), (925, 925)),
    ((1004, 1008), (926, 926)),
    ((1009, 1009), (928, 928)),
    ((1010, 1012), (929, 931)),
    ((1013, 1013), (932, 932)),
    ((1022, 1026), (945, 945)),
    ((1027, 1031), (946, 946)),
    ((1032, 1032), (948, 948)),
    ((1033, 1035), (949, 951)),
    ((1036, 1036), (952, 952)),
    ((1045, 1049), (964, 964)),
    ((1050, 1050), (966, 966)),
    ((1051, 1051), (967, 967)),
    ((1052, 1052), (968, 968)),
    ((1061, 1065), (980, 980)),
    ((1066, 1066), (982, 982)),
    ((1067, 1067), (983, 983)),
    ((1068, 1068), (984, 984)),
    ((1077, 1081), (997, 997)),
    ((1083, 1086), (999, 999)),
    ((1090, 1090), (1001, 1001)),
    ((1091, 1091), (1002, 1002)),
    ((1092, 1095), (1003, 1003)),
    ((1096, 1096), (1004, 1004)),
    ((1105, 1105), (1018, 1018)),
    ((1106, 1106), (1020, 1020)),
    ((1107, 1107), (1021, 1021)),
    ((1108, 1108), (1022, 1022)),
    ((1117, 1117), (1035, 1035)),
    ((1118, 1118), (1037, 1037)),
    ((1119, 1119), (1038, 1038)),
    ((1120, 1120), (1039, 1039)),
    ((1129, 1133), (1052, 1052)),
    ((1134, 1134), (1053, 1053)),
    ((1135, 1135), (1055, 1055)),
    ((1136, 1137), (1056, 1056)),
    ((1138, 1138), (1057, 1057)),
    ((1147, 1151), (1069, 1069)),
    ((1152, 1152), (1070, 1070)),
    ((1153, 1153), (1072, 1072)),
    ((1154, 1155), (1073, 1073)),
    ((1156, 1156), (1074, 1074)),
    ((1165, 1169), (1086, 1086)),
    ((1170, 1170), (1087, 1087)),
    ((1171, 1171), (1089, 1089)),
    ((1172, 1173), (1090, 1090)),
    ((1174, 1174), (1091, 1091)),
    ((1183, 1187), (1103, 1103)),
    ((1188, 1188), (1104, 1104)),
    ((1189, 1189), (1106, 1106)),
    ((1190, 1191), (1107, 1107)),
    ((1192, 1192), (1108, 1108)),
    ((1201, 1205), (1120, 1120)),
    ((1206, 1206), (1121, 1121)),
    ((1207, 1207), (1123, 1123)),
    ((1208, 1209), (1124, 1124)),
    ((1210, 1210), (1125, 1125)),
    ((1219, 1223), (1137, 1137)),
    ((1224, 1224), (1138, 1138)),
    ((1225, 1225), (1140, 1140)),
    ((1226, 1227), (1141, 1141)),
    ((1228, 1228), (1142, 1142)),
    ((1237, 1241), (1154, 1154)),
    ((1242, 1242), (1155, 1155)),
    ((1243, 1243), (1157, 1157)),
    ((1244, 1245), (1158, 1158)),
    ((1246, 1246), (1159, 1159)),
    ((1255, 1259), (1171, 1171)),
    ((1260, 1264), (1172, 1172)),
    ((1265, 1265), (1174, 1174)),
    ((1266, 1266), (1175, 1175)),
)
