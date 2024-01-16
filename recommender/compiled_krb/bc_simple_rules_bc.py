# bc_simple_rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def what_to_buy_under50k_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_office_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_office_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_office_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_office_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_office_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_office_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_office_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gaming_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gaming_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gaming_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gaming_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gaming_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gaming_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gaming_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50k_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50k_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50k_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50k_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50k_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50k_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50k_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_office_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_office_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_office_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_office_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_office_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_office_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_office_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gaming_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gaming_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gaming_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gaming_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gaming_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gaming_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gaming_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_office_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_office_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_office_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_office_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_office_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_office_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_office_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gaming_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_office_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_office_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_office_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_office_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_office_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_office_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_office_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gaming_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_office_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_office_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_office_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_office_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_office_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_office_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_office_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_gaming_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_gaming_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_gaming_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_gaming_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_gaming_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_gaming_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_gaming_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gc_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gc_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gc_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gc_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gc_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gc_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gc_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gc_office_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gc_office_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gc_office_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gc_office_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gc_office_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gc_office_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gc_office_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gc_gaming_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_office_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_gaming_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50K_gc_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_graphics', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_dell_windows: got unexpected plan from when clause 4"
                        if context.lookup_data('budget') in (2,):
                          if context.lookup_data('os') in (1,):
                            if context.lookup_data('brand') in (1,):
                              if context.lookup_data('ssd') in (2,):
                                if context.lookup_data('use') in (1,):
                                  rule.rule_base.num_bc_rule_successes += 1
                                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50K_gc_office_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_office_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_office_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_office_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_office_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_office_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_office_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50K_gc_gaming_dell_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50K_gc_gaming_dell_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (1,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_office_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_office_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_office_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_office_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_office_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_office_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_office_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gaming_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gaming_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gaming_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gaming_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gaming_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gaming_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gaming_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50k_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50k_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50k_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50k_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50k_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50k_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50k_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_office_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_office_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_office_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_office_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_office_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_office_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_office_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gaming_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gaming_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gaming_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gaming_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gaming_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gaming_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gaming_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_office_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_office_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_office_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_office_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_office_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_office_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_office_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gaming_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_office_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_office_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_office_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_office_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_office_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_office_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_office_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gaming_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_office_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_gaming_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50k_gc_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50k_gc_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50k_gc_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50k_gc_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50k_gc_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50k_gc_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50k_gc_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gc_office_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gc_office_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gc_office_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gc_office_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gc_office_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gc_office_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gc_office_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gc_gaming_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gc_gaming_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gc_gaming_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gc_gaming_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gc_gaming_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gc_gaming_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gc_gaming_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gc_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gc_office_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gc_gaming_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_office_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_gaming_lenovo_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_lenovo_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (2,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_office_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_office_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_office_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_office_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_office_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_office_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_office_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gaming_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gaming_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gaming_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gaming_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gaming_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gaming_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gaming_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50k_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50k_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50k_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50k_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50k_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50k_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50k_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_office_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_office_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_office_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_office_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_office_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_office_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_office_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gaming_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gaming_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gaming_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gaming_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gaming_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gaming_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gaming_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_office_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_office_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_office_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_office_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_office_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_office_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_office_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gaming_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_office_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_office_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_office_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_office_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_office_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_office_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_office_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gaming_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_office_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_office_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_office_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_office_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_office_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_office_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_office_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_gaming_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50k_gc_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50k_gc_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50k_gc_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50k_gc_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50k_gc_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50k_gc_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50k_gc_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gc_office_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gc_office_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gc_office_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gc_office_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gc_office_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gc_office_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gc_office_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gc_gaming_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gc_gaming_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gc_gaming_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gc_gaming_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gc_gaming_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gc_gaming_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gc_gaming_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gc_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gc_office_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gc_gaming_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_office_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_gaming_hp_windows(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_hp_windows: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_hp_windows: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_hp_windows: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_hp_windows: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_hp_windows: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_hp_windows: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (1,):
                                    if context.lookup_data('brand') in (3,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_office_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_office_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_office_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_office_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_office_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_office_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_office_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gaming_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gaming_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gaming_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gaming_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gaming_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gaming_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gaming_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50k_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50k_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50k_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50k_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50k_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50k_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50k_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (3,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_office_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_office_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_office_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_office_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_office_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_office_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_office_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gaming_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gaming_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gaming_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gaming_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gaming_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gaming_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gaming_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_office_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_office_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_office_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_office_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_office_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_office_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_office_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gaming_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gaming_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_office_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_office_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_office_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_office_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_office_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_office_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_office_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gaming_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gaming_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_office_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_office_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_office_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_office_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_office_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_office_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_office_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_under50k_gc_gaming_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50k_gc_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50k_gc_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50k_gc_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50k_gc_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50k_gc_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50k_gc_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50k_gc_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (3,):
                                  if context.lookup_data('os') in (3,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gc_office_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gc_office_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gc_office_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gc_office_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gc_office_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gc_office_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gc_office_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (3,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_above50K_gc_gaming_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_above50K_gc_gaming_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_above50K_gc_gaming_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_above50K_gc_gaming_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_above50K_gc_gaming_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_above50K_gc_gaming_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_above50K_gc_gaming_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (3,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (1,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gc_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gc_office_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_office_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_under50k_gc_gaming_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_under50k_gc_gaming_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (1,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_office_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_office_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (2,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_buy_ssd_512_above50k_gc_gaming_apple_macos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_budget', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_apple_macos: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_brand', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_apple_macos: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_os', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_apple_macos: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_ssd', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_apple_macos: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_use', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_apple_macos: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_graphics', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules.what_to_buy_ssd_512_above50k_gc_gaming_apple_macos: got unexpected plan from when clause 6"
                                if context.lookup_data('budget') in (2,):
                                  if context.lookup_data('os') in (2,):
                                    if context.lookup_data('brand') in (4,):
                                      if context.lookup_data('ssd') in (2,):
                                        if context.lookup_data('use') in (3,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules')
  
  bc_rule.bc_rule('what_to_buy_under50k_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_dell_windows, None,
                  (pattern.pattern_literal("Dell Latitude 7490 Laptop - Intel Core i7-8650U - 32GB DDR4 - 256GB SSD - 1. AMD Radeon RX 6600 XT - 14inches FHD Display - Backlit KB - Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_office_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_office_dell_windows, None,
                  (pattern.pattern_literal("Dell XPS 15 Laptop - Intel Core i9-12900HK - 32GB DDR5 - 256GB SSD - NVIDIA GeForce RTX 3050 Ti 4GB - Backlit KB - Fingerprint Reader - Windows 11 - 15.6 inches FHD+ Display - Platinum Silver - 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gaming_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gaming_dell_windows, None,
                  (pattern.pattern_literal("Dell Alienware Gaming m15 R7 - Intel Core i7-12700H, 256GB SSD, 16GB RAM, GeForce RTX 3070 Ti- 15.6-inch QHD 240Hz - Windows 11 - Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50k_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50k_dell_windows, None,
                  (pattern.pattern_literal("Dell G15 5520 - Intel Core i5-12500H - 8GB DDR5 - 256GB SSD - NVIDIA GeForce RTX 3050 4GB - Backlit KB - Windows 11 - 15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50K_office_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_office_dell_windows, None,
                  (pattern.pattern_literal("Dell Latitude 5530 Laptop - Intel Core i7-1270P 32GB DDR4 256GB SSD GeForce NVIDIA RTX-3070 Backlit KB 15.6 inches FHD Display Windows 11"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gaming_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gaming_dell_windows, None,
                  (pattern.pattern_literal("Dell Alienware m15 R7 Gaming Laptop - AMD Ryzen 9 6900HX - 32GB DDR5 - 256GB SSD - NVIDIA GeForce RTX 3080 Ti - Windows 11 - 15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_dell_windows, None,
                  (pattern.pattern_literal("Dell Latitude 7490 Laptop - Intel Core i7-8650U - 32GB DDR4 - 512GB SSD - GeForce RTX-1080 - 14inches FHD Display - Backlit KB - Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_office_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_office_dell_windows, None,
                  (pattern.pattern_literal("Dell Latitude 7490 Laptop - Intel Core i7-8650U - 32GB DDR4 - 512GB SSD - GeForce RTX-1080 - 14inches FHD Display - Backlit KB - Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gaming_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gaming_dell_windows, None,
                  (pattern.pattern_literal("Dell Alienware m15 R7 Gaming Laptop - AMD Ryzen 9 6900HX - 32GB DDR5 - 512GB SSD - NVIDIA GeForce RTX 3080 Ti - Windows 11 - 15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_dell_windows, None,
                  (pattern.pattern_literal("Dell G15 5520 - Intel Core i5-12500H - 8GB DDR5 - 512GB SSD - NVIDIA GeForce RTX 3050 4GB - Backlit KB - Windows 11 - 15.6 inches FHD 120Hz Display | Dark Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_office_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_office_dell_windows, None,
                  (pattern.pattern_literal("Dell Latitude 5530 Laptop - Intel Core i7-1270P 32GB DDR4 512GB SSD GeForce NVIDIA RTX-3070 Backlit KB 15.6 inches FHD Display Windows 11"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gaming_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gaming_dell_windows, None,
                  (pattern.pattern_literal("Dell XPS 15 9520 Core i9 12th Generation 32GB RAM 512GB SSD 4GB RTX 3050Ti Touch Windows 11 New"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_dell_windows, None,
                  (pattern.pattern_literal("Dell Latitude 7490 Laptop - Intel Core i7-8650U - 32GB DDR4 - 256GB SSD - Intel Graphics 5000 - 14inches FHD Display - Backlit KB - Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_office_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_office_dell_windows, None,
                  (pattern.pattern_literal("Dell XPS 15 Laptop - Intel Core i9-12900HK - 32GB DDR5 - 256GB SSD - Intel UHD Graphics 4000 - Backlit KB - Fingerprint Reader - Windows 11 - 15.6 inches FHD+ Display - Platinum Silver - 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_gaming_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_gaming_dell_windows, None,
                  (pattern.pattern_literal("Dell G15 5511 Gaming Laptop - Tiger Lake - 11th Gen Core i5 HexaCore Processor 16GB to 32GB 256SSD 4-GB Intel UHD 8000 15.6 inches Full HD 1080p 165Hz 300nits WVA AG Narrow Bezel Display Backlit KB W11 (Dark Shadow Grey)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gc_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gc_dell_windows, None,
                  (pattern.pattern_literal("Dell G15 5520 - Intel Core i5-12500H - 8GB DDR5 - 256GB SSD - 4GB - Backlit KB - Windows 11 - 15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gc_office_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gc_office_dell_windows, None,
                  (pattern.pattern_literal("Dell Latitude 5530 Laptop - Intel Core i7-1270P 32GB DDR4 256GB SSD Backlit KB 15.6 inches FHD Display Windows 11"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gc_gaming_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gc_gaming_dell_windows, None,
                  (pattern.pattern_literal("Dell Alienware m15 R7 Gaming Laptop - AMD Ryzen 9 6900HX - 32GB DDR5 - 256GB SSD - Windows 11 - 15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_dell_windows, None,
                  (pattern.pattern_literal("Dell G15 5520 - Intel Core i5-12500H - 8GB DDR5 - 512GB SSD - 4GB - Backlit KB - Windows 11 - 15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_office_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_office_dell_windows, None,
                  (pattern.pattern_literal("Dell Latitude 5530 Laptop - Intel Core i7-1270P 32GB DDR4 512GB SSD Backlit KB 15.6 inches FHD Display Windows 11"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_gaming_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_gaming_dell_windows, None,
                  (pattern.pattern_literal("Dell Alienware m15 R7 Gaming Laptop - AMD Ryzen 9 6900HX - 32GB DDR5 - 512GB SSD - Windows 11 - 15.6 inches QHD 240Hz 2ms| Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50K_gc_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50K_gc_dell_windows, None,
                  (pattern.pattern_literal("Dell G15 5520 - Intel Core i5-12500H - 8GB DDR5 - 512GB SSD - Intel UHD 7000 - Backlit KB - Windows 11 - 15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50K_gc_office_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50K_gc_office_dell_windows, None,
                  (pattern.pattern_literal("Dell Latitude 5530 Laptop - Intel Core i7-1270P 32GB DDR4 512GB SSD Backlit KB 15.6 inches FHD Display Windows 11"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50K_gc_gaming_dell_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50K_gc_gaming_dell_windows, None,
                  (pattern.pattern_literal("Dell XPS 15 9520 Core i9 12th Generation 32GB RAM 512GB SSD 4GB Touch Windows 11 New"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_under50k_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 300 i305,Intel Core i5 5th Generation,4GB DDR3,256GB SSD,Nvidia Quadro RTX 4000,14inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_office_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_office_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Chromebook Duet 2-In-1 Chromebook,MediaTek Helio P60T,32GB DDR5,256GB SSD,Nvidia Quadro RTX 5000,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gaming_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gaming_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo V14 IGL 82C2001QGE Gaming Laptop,Intel Core i7 5th Generation,8GB DDR5,256GB SSD,Nvidia GeForce GTX 1660 Ti,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50k_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50k_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 15,Intel Celeron,4GB DDR3,256GB SSD,MSI RTX 3090 Gaming X Trio,14inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50K_office_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_office_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 3,Intel Core i7,32GB DDR5,256GB SSD,AMD Radeon RX 6800,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gaming_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gaming_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo ThinkPad Gaming Laptop,Intel Core i9,32GB DDR5,256GB SSD,NVIDIA GeForce RTX 3080 Ti,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 300 i305,Intel Core i5 5th Generation,4GB DDR3,512GB SSD,Nvidia Quadro RTX 4000,14inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_office_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_office_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Chromebook Duet 2-In-1 Chromebook,MediaTek Helio P60T,32GB DDR5,512GB SSD,Nvidia Quadro RTX 5000,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gaming_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gaming_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo V14 IGL 82C2001QGE Gaming Laptop,Intel Core i7 5th Generation,8GB DDR5,512GB SSD,Nvidia GeForce GTX 1660 Ti,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 15,Intel Celeron,4GB DDR3,512GB SSD,MSI RTX 3090 Gaming X Trio,14inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_office_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_office_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 3,Intel Core i7,32GB DDR5,512GB SSD,AMD Radeon RX 6800,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gaming_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gaming_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo ThinkPad Gaming Laptop,Intel Core i9,32GB DDR5,512GB SSD,NVIDIA GeForce RTX 3080 Ti,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 300 i305,Intel Core i5 5th Generation,4GB DDR3,256GB SSD,14inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_office_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_office_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Chromebook Duet 2-In-1 Chromebook,MediaTek Helio P60T,32GB DDR5,256GB SSD,Intel UHD 5000,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_gaming_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_gaming_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo V14 IGL 82C2001QGE Gaming Laptop,Intel Core i7 5th Generation,8GB DDR5,256GB SSD,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50k_gc_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50k_gc_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 15,Intel Celeron,4GB DDR3,256GB SSD,14inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gc_office_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gc_office_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 3,Intel Core i7,32GB DDR5,256GB SSD,Intel UHD Graphics 6000,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gc_gaming_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gc_gaming_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo ThinkPad Gaming Laptop,Intel Core i9,32GB DDR5,256GB SSD,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gc_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gc_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 300 i305,Intel Core i5 5th Generation,4GB DDR3,512GB SSD,Intel Graphics 4000,14inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gc_office_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gc_office_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Chromebook Duet 2-In-1 Chromebook,MediaTek Helio P60T,32GB DDR5,512GB SSD,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gc_gaming_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gc_gaming_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo V14 IGL 82C2001QGE Gaming Laptop,Intel Core i7 5th Generation,8GB DDR5,512GB SSD,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 15,Intel Celeron,4GB DDR3,512GB SSD,14inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_office_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_office_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo Ideapad 3,Intel Core i7,32GB DDR5,512GB SSD,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_gaming_lenovo_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_gaming_lenovo_windows, None,
                  (pattern.pattern_literal("Lenovo ThinkPad Gaming Laptop,Intel Core i9,32GB DDR5,512GB SSD,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_under50k_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_hp_windows, None,
                  (pattern.pattern_literal("HP 14s DQ2100TU,Intel Core i3 11th Gen,8GB DDR3,256GB SSD,Nvidia Quadro 2000,18inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_office_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_office_hp_windows, None,
                  (pattern.pattern_literal("HP 15s dy3001TU,Core i5 5th Gen,16GB DDR5,256GB SSD,Nvidia Quadro RTX 8000,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gaming_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gaming_hp_windows, None,
                  (pattern.pattern_literal("HP 14sfq1092au Gaming Laptop,Ryzen 5 Hexa Core 5500U,32GB DDR5,256GB SSD,Nvidia GeForce GTX 1060,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50k_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50k_hp_windows, None,
                  (pattern.pattern_literal("HP ProBook 635 Aero G7,AMD Ryzen 7 4700U OctaCore,8GB DDR5,256GB SSD,MSI RTX 3090 Gaming X Duo,18inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50K_office_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_office_hp_windows, None,
                  (pattern.pattern_literal("HP EliteBook,Folio x360 1030 G3 8th Gen Ci5 QuadCore,32GB DDR5,256GB SSD,Nvidia GeForce RTX 3080 Ti,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gaming_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gaming_hp_windows, None,
                  (pattern.pattern_literal("HP EliteBook 830 Gaming Laptop,G5 8th Gen Ci5 QuadCore,64GB DDR5,256GB SSD,NVIDIA GeForce RTX 4080 Ti,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_hp_windows, None,
                  (pattern.pattern_literal("HP 14s DQ2100TU,Intel Core i3 11th Gen,8GB DDR3,512GB SSD,Nvidia Quadro 2000,18inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_office_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_office_hp_windows, None,
                  (pattern.pattern_literal("HP 15s dy3001TU,Core i5 5th Gen,16GB DDR5,512GB SSD,Nvidia Quadro RTX 8000,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gaming_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gaming_hp_windows, None,
                  (pattern.pattern_literal("HP 14sfq1092au Gaming Laptop,Ryzen 5 Hexa Core 5500U,32GB DDR5,512GB SSD,Nvidia GeForce GTX 1060,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_hp_windows, None,
                  (pattern.pattern_literal("HP ProBook 635 Aero G7,AMD Ryzen 7 4700U OctaCore,8GB DDR5,512GB SSD,MSI RTX 3090 Gaming X Duo,18inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_office_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_office_hp_windows, None,
                  (pattern.pattern_literal("HP EliteBook,Folio x360 1030 G3 8th Gen Ci5 QuadCore,32GB DDR5,512GB SSD,Nvidia GeForce RTX 3080 Ti,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gaming_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gaming_hp_windows, None,
                  (pattern.pattern_literal("HP EliteBook 830 Gaming Laptop,G5 8th Gen Ci5 QuadCore,64GB DDR5,512GB SSD,NVIDIA GeForce RTX 4080 Ti,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_hp_windows, None,
                  (pattern.pattern_literal("HP 14s DQ2100TU,Intel Core i3 11th Gen,8GB DDR3,256GB SSD,18inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_office_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_office_hp_windows, None,
                  (pattern.pattern_literal("HP 15s dy3001TU,Core i5 5th Gen,16GB DDR5,256GB SSD,Intel UHD 4000,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_gaming_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_gaming_hp_windows, None,
                  (pattern.pattern_literal("HP 14sfq1092au Gaming Laptop,Ryzen 5 Hexa Core 5500U,32GB DDR5,256GB SSD,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50k_gc_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50k_gc_hp_windows, None,
                  (pattern.pattern_literal("HP ProBook 635 Aero G7,AMD Ryzen 7 4700U OctaCore,8GB DDR5,256GB SSD,18inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gc_office_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gc_office_hp_windows, None,
                  (pattern.pattern_literal("HP EliteBook,Folio x360 1030 G3 8th Gen Ci5 QuadCore,32GB DDR5,256GB SSD,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gc_gaming_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gc_gaming_hp_windows, None,
                  (pattern.pattern_literal("HP EliteBook 830 Gaming Laptop,G5 8th Gen Ci5 QuadCore,64GB DDR5,256GB SSD,Intel UHD Graphics 8000,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gc_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gc_hp_windows, None,
                  (pattern.pattern_literal("HP 14s DQ2100TU,Intel Core i3 11th Gen,8GB DDR3,512GB SSD,18inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gc_office_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gc_office_hp_windows, None,
                  (pattern.pattern_literal("HP 15s dy3001TU,Core i5 5th Gen,16GB DDR5,512GB SSD,Intel UHD 5000,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gc_gaming_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gc_gaming_hp_windows, None,
                  (pattern.pattern_literal("HP 14sfq1092au Gaming Laptop,Ryzen 5 Hexa Core 5500U,32GB DDR5,512GB SSD,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_hp_windows, None,
                  (pattern.pattern_literal("HP ProBook 635 Aero G7,AMD Ryzen 7 4700U OctaCore,8GB DDR5,512GB SSD,Intel UHD 5000,18inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_office_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_office_hp_windows, None,
                  (pattern.pattern_literal("HP EliteBook,Folio x360 1030 G3 8th Gen Ci5 QuadCore,32GB DDR5,512GB SSD,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_gaming_hp_windows', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_gaming_hp_windows, None,
                  (pattern.pattern_literal("HP EliteBook 830 Gaming Laptop,G5 8th Gen Ci5 QuadCore,64GB DDR5,512GB SSD,Intel UHD Graphics 4000,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_under50k_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air 2020 Z0YL00174,10th Gen Core I5,8GB DDR5,256GB SSD,Nvidia Quadro RTX 4000,16inches Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_office_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_office_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MQD32HN,Core i5 11th Gen,16GB DDR5,256GB SSD,Nvidia Geforce GTX 4000,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gaming_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gaming_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MWTK2HN Gaming Laptop,1GHz dual core 10th generation,16GB DDR5,256GB SSD,Nvidia GeForce GTX 1080 ti,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50k_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_above50k_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air M1 MGN63HN Ultrabook,AMD Ryzen 16 5300U OctaCore,32GB DDR5,256GB SSD,RTX 3090 ti,24inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50K_office_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_office_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air 2022,8 core GPU 16 core Neural Engine,32GB DDR5,256GB SSD,MSI GeForce RTX 3070,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gaming_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gaming_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MVFJ2HN Gaming Laptop,8th Gen Core I9,64GB DDR5,256GB SSD,NVIDIA GeForce RTX 4080 Ti,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air 2020 Z0YL00174,10th Gen Core I5,8GB DDR5,512GB SSD,Nvidia Quadro RTX 4000,16inches Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_office_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_office_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MQD32HN,Core i5 11th Gen,16GB DDR5,512GB SSD,Nvidia Geforce GTX 4000,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gaming_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gaming_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MWTK2HN Gaming Laptop,1GHz dual core 10th generation,16GB DDR5,512GB SSD,Nvidia GeForce GTX 1080 ti,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air M1 MGN63HN Ultrabook,AMD Ryzen 16 5300U OctaCore,32GB DDR5,512GB SSD,RTX 3090 ti,24inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_office_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_office_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air 2022,8 core GPU 16 core Neural Engine,32GB DDR5,512GB SSD,MSI GeForce RTX 3070,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gaming_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gaming_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MVFJ2HN Gaming Laptop,8th Gen Core I9,64GB DDR5,512GB SSD,NVIDIA GeForce RTX 4080 Ti,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air 2020 Z0YL00174,10th Gen Core I5,8GB DDR5,256GB SSD,16inches Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_office_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_office_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MQD32HN,Core i5 11th Gen,16GB DDR5,256GB SSD,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_under50k_gc_gaming_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_under50k_gc_gaming_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MWTK2HN Gaming Laptop,1GHz dual core 10th generation,16GB DDR5,256GB SSD,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50k_gc_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_above50k_gc_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air M1 MGN63HN Ultrabook,AMD Ryzen 16 5300U OctaCore,32GB DDR5,256GB SSD,24inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gc_office_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gc_office_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air 2022,8 core GPU 16 core Neural Engine,32GB DDR5,256GB SSD,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_above50K_gc_gaming_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_above50K_gc_gaming_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MVFJ2HN Gaming Laptop,8th Gen Core I9,64GB DDR5,256GB SSD,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gc_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gc_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air 2020 Z0YL00174,10th Gen Core I5,8GB DDR5,512GB SSD,16inches Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gc_office_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gc_office_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MQD32HN,Core i5 11th Gen,16GB DDR5,512GB SSD,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_under50k_gc_gaming_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_under50k_gc_gaming_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MWTK2HN Gaming Laptop,1GHz dual core 10th generation,16GB DDR5,512GB SSD,Backlit KB,Windows 11,15.6 inches FHD 120Hz Display | Dark Shadow Grey"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air M1 MGN63HN Ultrabook,AMD Ryzen 16 5300U OctaCore,32GB DDR5,512GB SSD,24inches FHD Display,Backlit KB,Fingerprint Reader (Open Box)"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_office_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_office_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air 2022,8 core GPU 16 core Neural Engine,32GB DDR5,512GB SSD,Backlit KB,Fingerprint Reader,Windows 11,15.6 inches FHD+ Display,Platinum Silver 9520"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_buy_ssd_512_above50k_gc_gaming_apple_macos', This_rule_base, 'what_to_buy',
                  what_to_buy_ssd_512_above50k_gc_gaming_apple_macos, None,
                  (pattern.pattern_literal("Apple MacBook Air MVFJ2HN Gaming Laptop,8th Gen Core I9,64GB DDR5,512GB SSD,Windows 11,15.6 inches QHD 240Hz 2ms NVIDIA G-SYNC Display | Dark Side of the Moon"),),
                  (),
                  (contexts.variable('budget'),
                   contexts.variable('brand'),
                   contexts.variable('os'),
                   contexts.variable('ssd'),
                   contexts.variable('use'),
                   pattern.pattern_literal(False),))


Krb_filename = '..\\bc_simple_rules.krb'
Krb_lineno_map = (
    ((14, 18), (5, 5)),
    ((20, 25), (7, 7)),
    ((26, 31), (8, 8)),
    ((32, 37), (9, 9)),
    ((38, 43), (10, 10)),
    ((44, 49), (11, 11)),
    ((50, 55), (12, 12)),
    ((56, 56), (13, 13)),
    ((57, 57), (14, 14)),
    ((58, 58), (15, 15)),
    ((59, 59), (16, 16)),
    ((60, 60), (17, 17)),
    ((73, 77), (20, 20)),
    ((79, 84), (22, 22)),
    ((85, 90), (23, 23)),
    ((91, 96), (24, 24)),
    ((97, 102), (25, 25)),
    ((103, 108), (26, 26)),
    ((109, 114), (27, 27)),
    ((115, 115), (28, 28)),
    ((116, 116), (29, 29)),
    ((117, 117), (30, 30)),
    ((118, 118), (31, 31)),
    ((119, 119), (32, 32)),
    ((132, 136), (36, 36)),
    ((138, 143), (38, 38)),
    ((144, 149), (39, 39)),
    ((150, 155), (40, 40)),
    ((156, 161), (41, 41)),
    ((162, 167), (42, 42)),
    ((168, 173), (43, 43)),
    ((174, 174), (44, 44)),
    ((175, 175), (45, 45)),
    ((176, 176), (46, 46)),
    ((177, 177), (47, 47)),
    ((178, 178), (48, 48)),
    ((191, 195), (52, 52)),
    ((197, 202), (54, 54)),
    ((203, 208), (55, 55)),
    ((209, 214), (56, 56)),
    ((215, 220), (57, 57)),
    ((221, 226), (58, 58)),
    ((227, 232), (59, 59)),
    ((233, 233), (60, 60)),
    ((234, 234), (61, 61)),
    ((235, 235), (62, 62)),
    ((236, 236), (63, 63)),
    ((237, 237), (64, 64)),
    ((250, 254), (67, 67)),
    ((256, 261), (69, 69)),
    ((262, 267), (70, 70)),
    ((268, 273), (71, 71)),
    ((274, 279), (72, 72)),
    ((280, 285), (73, 73)),
    ((286, 291), (74, 74)),
    ((292, 292), (75, 75)),
    ((293, 293), (76, 76)),
    ((294, 294), (77, 77)),
    ((295, 295), (78, 78)),
    ((296, 296), (79, 79)),
    ((309, 313), (82, 82)),
    ((315, 320), (84, 84)),
    ((321, 326), (85, 85)),
    ((327, 332), (86, 86)),
    ((333, 338), (87, 87)),
    ((339, 344), (88, 88)),
    ((345, 350), (89, 89)),
    ((351, 351), (90, 90)),
    ((352, 352), (91, 91)),
    ((353, 353), (92, 92)),
    ((354, 354), (93, 93)),
    ((355, 355), (94, 94)),
    ((368, 372), (98, 98)),
    ((374, 379), (100, 100)),
    ((380, 385), (101, 101)),
    ((386, 391), (102, 102)),
    ((392, 397), (103, 103)),
    ((398, 403), (104, 104)),
    ((404, 409), (105, 105)),
    ((410, 410), (106, 106)),
    ((411, 411), (107, 107)),
    ((412, 412), (108, 108)),
    ((413, 413), (109, 109)),
    ((414, 414), (110, 110)),
    ((427, 431), (113, 113)),
    ((433, 438), (115, 115)),
    ((439, 444), (116, 116)),
    ((445, 450), (117, 117)),
    ((451, 456), (118, 118)),
    ((457, 462), (119, 119)),
    ((463, 468), (120, 120)),
    ((469, 469), (121, 121)),
    ((470, 470), (122, 122)),
    ((471, 471), (123, 123)),
    ((472, 472), (124, 124)),
    ((473, 473), (125, 125)),
    ((486, 490), (129, 129)),
    ((492, 497), (131, 131)),
    ((498, 503), (132, 132)),
    ((504, 509), (133, 133)),
    ((510, 515), (134, 134)),
    ((516, 521), (135, 135)),
    ((522, 527), (136, 136)),
    ((528, 528), (137, 137)),
    ((529, 529), (138, 138)),
    ((530, 530), (139, 139)),
    ((531, 531), (140, 140)),
    ((532, 532), (141, 141)),
    ((545, 549), (144, 144)),
    ((551, 556), (146, 146)),
    ((557, 562), (147, 147)),
    ((563, 568), (148, 148)),
    ((569, 574), (149, 149)),
    ((575, 580), (150, 150)),
    ((581, 586), (151, 151)),
    ((587, 587), (152, 152)),
    ((588, 588), (153, 153)),
    ((589, 589), (154, 154)),
    ((590, 590), (155, 155)),
    ((591, 591), (156, 156)),
    ((604, 608), (159, 159)),
    ((610, 615), (161, 161)),
    ((616, 621), (162, 162)),
    ((622, 627), (163, 163)),
    ((628, 633), (164, 164)),
    ((634, 639), (165, 165)),
    ((640, 645), (166, 166)),
    ((646, 646), (167, 167)),
    ((647, 647), (168, 168)),
    ((648, 648), (169, 169)),
    ((649, 649), (170, 170)),
    ((650, 650), (171, 171)),
    ((663, 667), (175, 175)),
    ((669, 674), (177, 177)),
    ((675, 680), (178, 178)),
    ((681, 686), (179, 179)),
    ((687, 692), (180, 180)),
    ((693, 698), (181, 181)),
    ((699, 704), (182, 182)),
    ((705, 705), (183, 183)),
    ((706, 706), (184, 184)),
    ((707, 707), (185, 185)),
    ((708, 708), (186, 186)),
    ((709, 709), (187, 187)),
    ((722, 726), (194, 194)),
    ((728, 733), (196, 196)),
    ((734, 739), (197, 197)),
    ((740, 745), (198, 198)),
    ((746, 751), (199, 199)),
    ((752, 757), (200, 200)),
    ((758, 763), (201, 201)),
    ((764, 764), (202, 202)),
    ((765, 765), (203, 203)),
    ((766, 766), (204, 204)),
    ((767, 767), (205, 205)),
    ((768, 768), (206, 206)),
    ((781, 785), (209, 209)),
    ((787, 792), (211, 211)),
    ((793, 798), (212, 212)),
    ((799, 804), (213, 213)),
    ((805, 810), (214, 214)),
    ((811, 816), (215, 215)),
    ((817, 822), (216, 216)),
    ((823, 823), (217, 217)),
    ((824, 824), (218, 218)),
    ((825, 825), (219, 219)),
    ((826, 826), (220, 220)),
    ((827, 827), (221, 221)),
    ((840, 844), (225, 225)),
    ((846, 851), (227, 227)),
    ((852, 857), (228, 228)),
    ((858, 863), (229, 229)),
    ((864, 869), (230, 230)),
    ((870, 875), (231, 231)),
    ((876, 881), (232, 232)),
    ((882, 882), (233, 233)),
    ((883, 883), (234, 234)),
    ((884, 884), (235, 235)),
    ((885, 885), (236, 236)),
    ((886, 886), (237, 237)),
    ((899, 903), (241, 241)),
    ((905, 910), (243, 243)),
    ((911, 916), (244, 244)),
    ((917, 922), (245, 245)),
    ((923, 928), (246, 246)),
    ((929, 934), (247, 247)),
    ((935, 940), (248, 248)),
    ((941, 941), (249, 249)),
    ((942, 942), (250, 250)),
    ((943, 943), (251, 251)),
    ((944, 944), (252, 252)),
    ((945, 945), (253, 253)),
    ((958, 962), (256, 256)),
    ((964, 969), (258, 258)),
    ((970, 975), (259, 259)),
    ((976, 981), (260, 260)),
    ((982, 987), (261, 261)),
    ((988, 993), (262, 262)),
    ((994, 999), (263, 263)),
    ((1000, 1000), (264, 264)),
    ((1001, 1001), (265, 265)),
    ((1002, 1002), (266, 266)),
    ((1003, 1003), (267, 267)),
    ((1004, 1004), (268, 268)),
    ((1017, 1021), (271, 271)),
    ((1023, 1028), (273, 273)),
    ((1029, 1034), (274, 274)),
    ((1035, 1040), (275, 275)),
    ((1041, 1046), (276, 276)),
    ((1047, 1052), (277, 277)),
    ((1053, 1058), (278, 278)),
    ((1059, 1059), (279, 279)),
    ((1060, 1060), (280, 280)),
    ((1061, 1061), (281, 281)),
    ((1062, 1062), (282, 282)),
    ((1063, 1063), (283, 283)),
    ((1076, 1080), (287, 287)),
    ((1082, 1087), (289, 289)),
    ((1088, 1093), (290, 290)),
    ((1094, 1099), (291, 291)),
    ((1100, 1105), (292, 292)),
    ((1106, 1111), (293, 293)),
    ((1112, 1117), (294, 294)),
    ((1118, 1118), (295, 295)),
    ((1119, 1119), (296, 296)),
    ((1120, 1120), (297, 297)),
    ((1121, 1121), (298, 298)),
    ((1122, 1122), (299, 299)),
    ((1135, 1139), (302, 302)),
    ((1141, 1146), (304, 304)),
    ((1147, 1152), (305, 305)),
    ((1153, 1158), (306, 306)),
    ((1159, 1164), (307, 307)),
    ((1165, 1170), (308, 308)),
    ((1171, 1176), (309, 309)),
    ((1177, 1177), (310, 310)),
    ((1178, 1178), (311, 311)),
    ((1179, 1179), (312, 312)),
    ((1180, 1180), (313, 313)),
    ((1181, 1181), (314, 314)),
    ((1194, 1198), (317, 317)),
    ((1200, 1205), (319, 319)),
    ((1206, 1211), (320, 320)),
    ((1212, 1217), (321, 321)),
    ((1218, 1223), (322, 322)),
    ((1224, 1229), (323, 323)),
    ((1230, 1235), (324, 324)),
    ((1236, 1236), (325, 325)),
    ((1237, 1237), (326, 326)),
    ((1238, 1238), (327, 327)),
    ((1239, 1239), (328, 328)),
    ((1240, 1240), (329, 329)),
    ((1253, 1257), (333, 333)),
    ((1259, 1264), (335, 335)),
    ((1265, 1270), (336, 336)),
    ((1271, 1276), (337, 337)),
    ((1277, 1282), (338, 338)),
    ((1283, 1283), (339, 339)),
    ((1284, 1284), (340, 340)),
    ((1285, 1285), (341, 341)),
    ((1286, 1286), (342, 342)),
    ((1287, 1287), (343, 343)),
    ((1300, 1304), (346, 346)),
    ((1306, 1311), (348, 348)),
    ((1312, 1317), (349, 349)),
    ((1318, 1323), (350, 350)),
    ((1324, 1329), (351, 351)),
    ((1330, 1335), (352, 352)),
    ((1336, 1341), (353, 353)),
    ((1342, 1342), (354, 354)),
    ((1343, 1343), (355, 355)),
    ((1344, 1344), (356, 356)),
    ((1345, 1345), (357, 357)),
    ((1346, 1346), (358, 358)),
    ((1359, 1363), (362, 362)),
    ((1365, 1370), (364, 364)),
    ((1371, 1376), (365, 365)),
    ((1377, 1382), (366, 366)),
    ((1383, 1388), (367, 367)),
    ((1389, 1394), (368, 368)),
    ((1395, 1400), (369, 369)),
    ((1401, 1401), (370, 370)),
    ((1402, 1402), (371, 371)),
    ((1403, 1403), (372, 372)),
    ((1404, 1404), (373, 373)),
    ((1405, 1405), (374, 374)),
    ((1418, 1422), (382, 382)),
    ((1424, 1429), (384, 384)),
    ((1430, 1435), (385, 385)),
    ((1436, 1441), (386, 386)),
    ((1442, 1447), (387, 387)),
    ((1448, 1453), (388, 388)),
    ((1454, 1459), (389, 389)),
    ((1460, 1460), (390, 390)),
    ((1461, 1461), (391, 391)),
    ((1462, 1462), (392, 392)),
    ((1463, 1463), (393, 393)),
    ((1464, 1464), (394, 394)),
    ((1477, 1481), (397, 397)),
    ((1483, 1488), (399, 399)),
    ((1489, 1494), (400, 400)),
    ((1495, 1500), (401, 401)),
    ((1501, 1506), (402, 402)),
    ((1507, 1512), (403, 403)),
    ((1513, 1518), (404, 404)),
    ((1519, 1519), (405, 405)),
    ((1520, 1520), (406, 406)),
    ((1521, 1521), (407, 407)),
    ((1522, 1522), (408, 408)),
    ((1523, 1523), (409, 409)),
    ((1536, 1540), (413, 413)),
    ((1542, 1547), (415, 415)),
    ((1548, 1553), (416, 416)),
    ((1554, 1559), (417, 417)),
    ((1560, 1565), (418, 418)),
    ((1566, 1571), (419, 419)),
    ((1572, 1577), (420, 420)),
    ((1578, 1578), (421, 421)),
    ((1579, 1579), (422, 422)),
    ((1580, 1580), (423, 423)),
    ((1581, 1581), (424, 424)),
    ((1582, 1582), (425, 425)),
    ((1595, 1599), (429, 429)),
    ((1601, 1606), (431, 431)),
    ((1607, 1612), (432, 432)),
    ((1613, 1618), (433, 433)),
    ((1619, 1624), (434, 434)),
    ((1625, 1630), (435, 435)),
    ((1631, 1636), (436, 436)),
    ((1637, 1637), (437, 437)),
    ((1638, 1638), (438, 438)),
    ((1639, 1639), (439, 439)),
    ((1640, 1640), (440, 440)),
    ((1641, 1641), (441, 441)),
    ((1654, 1658), (444, 444)),
    ((1660, 1665), (446, 446)),
    ((1666, 1671), (447, 447)),
    ((1672, 1677), (448, 448)),
    ((1678, 1683), (449, 449)),
    ((1684, 1689), (450, 450)),
    ((1690, 1695), (451, 451)),
    ((1696, 1696), (452, 452)),
    ((1697, 1697), (453, 453)),
    ((1698, 1698), (454, 454)),
    ((1699, 1699), (455, 455)),
    ((1700, 1700), (456, 456)),
    ((1713, 1717), (459, 459)),
    ((1719, 1724), (461, 461)),
    ((1725, 1730), (462, 462)),
    ((1731, 1736), (463, 463)),
    ((1737, 1742), (464, 464)),
    ((1743, 1748), (465, 465)),
    ((1749, 1754), (466, 466)),
    ((1755, 1755), (467, 467)),
    ((1756, 1756), (468, 468)),
    ((1757, 1757), (469, 469)),
    ((1758, 1758), (470, 470)),
    ((1759, 1759), (471, 471)),
    ((1772, 1776), (474, 474)),
    ((1778, 1783), (476, 476)),
    ((1784, 1789), (477, 477)),
    ((1790, 1795), (478, 478)),
    ((1796, 1801), (479, 479)),
    ((1802, 1807), (480, 480)),
    ((1808, 1813), (481, 481)),
    ((1814, 1814), (482, 482)),
    ((1815, 1815), (483, 483)),
    ((1816, 1816), (484, 484)),
    ((1817, 1817), (485, 485)),
    ((1818, 1818), (486, 486)),
    ((1831, 1835), (489, 489)),
    ((1837, 1842), (491, 491)),
    ((1843, 1848), (492, 492)),
    ((1849, 1854), (493, 493)),
    ((1855, 1860), (494, 494)),
    ((1861, 1866), (495, 495)),
    ((1867, 1872), (496, 496)),
    ((1873, 1873), (497, 497)),
    ((1874, 1874), (498, 498)),
    ((1875, 1875), (499, 499)),
    ((1876, 1876), (500, 500)),
    ((1877, 1877), (501, 501)),
    ((1890, 1894), (505, 505)),
    ((1896, 1901), (507, 507)),
    ((1902, 1907), (508, 508)),
    ((1908, 1913), (509, 509)),
    ((1914, 1919), (510, 510)),
    ((1920, 1925), (511, 511)),
    ((1926, 1931), (512, 512)),
    ((1932, 1932), (513, 513)),
    ((1933, 1933), (514, 514)),
    ((1934, 1934), (515, 515)),
    ((1935, 1935), (516, 516)),
    ((1936, 1936), (517, 517)),
    ((1949, 1953), (520, 520)),
    ((1955, 1960), (522, 522)),
    ((1961, 1966), (523, 523)),
    ((1967, 1972), (524, 524)),
    ((1973, 1978), (525, 525)),
    ((1979, 1984), (526, 526)),
    ((1985, 1990), (527, 527)),
    ((1991, 1991), (528, 528)),
    ((1992, 1992), (529, 529)),
    ((1993, 1993), (530, 530)),
    ((1994, 1994), (531, 531)),
    ((1995, 1995), (532, 532)),
    ((2008, 2012), (535, 535)),
    ((2014, 2019), (537, 537)),
    ((2020, 2025), (538, 538)),
    ((2026, 2031), (539, 539)),
    ((2032, 2037), (540, 540)),
    ((2038, 2043), (541, 541)),
    ((2044, 2049), (542, 542)),
    ((2050, 2050), (543, 543)),
    ((2051, 2051), (544, 544)),
    ((2052, 2052), (545, 545)),
    ((2053, 2053), (546, 546)),
    ((2054, 2054), (547, 547)),
    ((2067, 2071), (551, 551)),
    ((2073, 2078), (553, 553)),
    ((2079, 2084), (554, 554)),
    ((2085, 2090), (555, 555)),
    ((2091, 2096), (556, 556)),
    ((2097, 2102), (557, 557)),
    ((2103, 2108), (558, 558)),
    ((2109, 2109), (559, 559)),
    ((2110, 2110), (560, 560)),
    ((2111, 2111), (561, 561)),
    ((2112, 2112), (562, 562)),
    ((2113, 2113), (563, 563)),
    ((2126, 2130), (571, 571)),
    ((2132, 2137), (573, 573)),
    ((2138, 2143), (574, 574)),
    ((2144, 2149), (575, 575)),
    ((2150, 2155), (576, 576)),
    ((2156, 2161), (577, 577)),
    ((2162, 2167), (578, 578)),
    ((2168, 2168), (579, 579)),
    ((2169, 2169), (580, 580)),
    ((2170, 2170), (581, 581)),
    ((2171, 2171), (582, 582)),
    ((2172, 2172), (583, 583)),
    ((2185, 2189), (586, 586)),
    ((2191, 2196), (588, 588)),
    ((2197, 2202), (589, 589)),
    ((2203, 2208), (590, 590)),
    ((2209, 2214), (591, 591)),
    ((2215, 2220), (592, 592)),
    ((2221, 2226), (593, 593)),
    ((2227, 2227), (594, 594)),
    ((2228, 2228), (595, 595)),
    ((2229, 2229), (596, 596)),
    ((2230, 2230), (597, 597)),
    ((2231, 2231), (598, 598)),
    ((2244, 2248), (602, 602)),
    ((2250, 2255), (604, 604)),
    ((2256, 2261), (605, 605)),
    ((2262, 2267), (606, 606)),
    ((2268, 2273), (607, 607)),
    ((2274, 2279), (608, 608)),
    ((2280, 2285), (609, 609)),
    ((2286, 2286), (610, 610)),
    ((2287, 2287), (611, 611)),
    ((2288, 2288), (612, 612)),
    ((2289, 2289), (613, 613)),
    ((2290, 2290), (614, 614)),
    ((2303, 2307), (618, 618)),
    ((2309, 2314), (620, 620)),
    ((2315, 2320), (621, 621)),
    ((2321, 2326), (622, 622)),
    ((2327, 2332), (623, 623)),
    ((2333, 2338), (624, 624)),
    ((2339, 2344), (625, 625)),
    ((2345, 2345), (626, 626)),
    ((2346, 2346), (627, 627)),
    ((2347, 2347), (628, 628)),
    ((2348, 2348), (629, 629)),
    ((2349, 2349), (630, 630)),
    ((2362, 2366), (633, 633)),
    ((2368, 2373), (635, 635)),
    ((2374, 2379), (636, 636)),
    ((2380, 2385), (637, 637)),
    ((2386, 2391), (638, 638)),
    ((2392, 2397), (639, 639)),
    ((2398, 2403), (640, 640)),
    ((2404, 2404), (641, 641)),
    ((2405, 2405), (642, 642)),
    ((2406, 2406), (643, 643)),
    ((2407, 2407), (644, 644)),
    ((2408, 2408), (645, 645)),
    ((2421, 2425), (648, 648)),
    ((2427, 2432), (650, 650)),
    ((2433, 2438), (651, 651)),
    ((2439, 2444), (652, 652)),
    ((2445, 2450), (653, 653)),
    ((2451, 2456), (654, 654)),
    ((2457, 2462), (655, 655)),
    ((2463, 2463), (656, 656)),
    ((2464, 2464), (657, 657)),
    ((2465, 2465), (658, 658)),
    ((2466, 2466), (659, 659)),
    ((2467, 2467), (660, 660)),
    ((2480, 2484), (663, 663)),
    ((2486, 2491), (665, 665)),
    ((2492, 2497), (666, 666)),
    ((2498, 2503), (667, 667)),
    ((2504, 2509), (668, 668)),
    ((2510, 2515), (669, 669)),
    ((2516, 2521), (670, 670)),
    ((2522, 2522), (671, 671)),
    ((2523, 2523), (672, 672)),
    ((2524, 2524), (673, 673)),
    ((2525, 2525), (674, 674)),
    ((2526, 2526), (675, 675)),
    ((2539, 2543), (678, 678)),
    ((2545, 2550), (680, 680)),
    ((2551, 2556), (681, 681)),
    ((2557, 2562), (682, 682)),
    ((2563, 2568), (683, 683)),
    ((2569, 2574), (684, 684)),
    ((2575, 2580), (685, 685)),
    ((2581, 2581), (686, 686)),
    ((2582, 2582), (687, 687)),
    ((2583, 2583), (688, 688)),
    ((2584, 2584), (689, 689)),
    ((2585, 2585), (690, 690)),
    ((2598, 2602), (694, 694)),
    ((2604, 2609), (696, 696)),
    ((2610, 2615), (697, 697)),
    ((2616, 2621), (698, 698)),
    ((2622, 2627), (699, 699)),
    ((2628, 2633), (700, 700)),
    ((2634, 2639), (701, 701)),
    ((2640, 2640), (702, 702)),
    ((2641, 2641), (703, 703)),
    ((2642, 2642), (704, 704)),
    ((2643, 2643), (705, 705)),
    ((2644, 2644), (706, 706)),
    ((2657, 2661), (709, 709)),
    ((2663, 2668), (711, 711)),
    ((2669, 2674), (712, 712)),
    ((2675, 2680), (713, 713)),
    ((2681, 2686), (714, 714)),
    ((2687, 2692), (715, 715)),
    ((2693, 2698), (716, 716)),
    ((2699, 2699), (717, 717)),
    ((2700, 2700), (718, 718)),
    ((2701, 2701), (719, 719)),
    ((2702, 2702), (720, 720)),
    ((2703, 2703), (721, 721)),
    ((2716, 2720), (724, 724)),
    ((2722, 2727), (726, 726)),
    ((2728, 2733), (727, 727)),
    ((2734, 2739), (728, 728)),
    ((2740, 2745), (729, 729)),
    ((2746, 2751), (730, 730)),
    ((2752, 2757), (731, 731)),
    ((2758, 2758), (732, 732)),
    ((2759, 2759), (733, 733)),
    ((2760, 2760), (734, 734)),
    ((2761, 2761), (735, 735)),
    ((2762, 2762), (736, 736)),
    ((2775, 2779), (740, 740)),
    ((2781, 2786), (742, 742)),
    ((2787, 2792), (743, 743)),
    ((2793, 2798), (744, 744)),
    ((2799, 2804), (745, 745)),
    ((2805, 2810), (746, 746)),
    ((2811, 2816), (747, 747)),
    ((2817, 2817), (748, 748)),
    ((2818, 2818), (749, 749)),
    ((2819, 2819), (750, 750)),
    ((2820, 2820), (751, 751)),
    ((2821, 2821), (752, 752)),
    ((2834, 2838), (761, 761)),
    ((2840, 2845), (763, 763)),
    ((2846, 2851), (764, 764)),
    ((2852, 2857), (765, 765)),
    ((2858, 2863), (766, 766)),
    ((2864, 2869), (767, 767)),
    ((2870, 2875), (768, 768)),
    ((2876, 2876), (769, 769)),
    ((2877, 2877), (770, 770)),
    ((2878, 2878), (771, 771)),
    ((2879, 2879), (772, 772)),
    ((2880, 2880), (773, 773)),
    ((2893, 2897), (776, 776)),
    ((2899, 2904), (778, 778)),
    ((2905, 2910), (779, 779)),
    ((2911, 2916), (780, 780)),
    ((2917, 2922), (781, 781)),
    ((2923, 2928), (782, 782)),
    ((2929, 2934), (783, 783)),
    ((2935, 2935), (784, 784)),
    ((2936, 2936), (785, 785)),
    ((2937, 2937), (786, 786)),
    ((2938, 2938), (787, 787)),
    ((2939, 2939), (788, 788)),
    ((2952, 2956), (792, 792)),
    ((2958, 2963), (794, 794)),
    ((2964, 2969), (795, 795)),
    ((2970, 2975), (796, 796)),
    ((2976, 2981), (797, 797)),
    ((2982, 2987), (798, 798)),
    ((2988, 2993), (799, 799)),
    ((2994, 2994), (800, 800)),
    ((2995, 2995), (801, 801)),
    ((2996, 2996), (802, 802)),
    ((2997, 2997), (803, 803)),
    ((2998, 2998), (804, 804)),
    ((3011, 3015), (808, 808)),
    ((3017, 3022), (810, 810)),
    ((3023, 3028), (811, 811)),
    ((3029, 3034), (812, 812)),
    ((3035, 3040), (813, 813)),
    ((3041, 3046), (814, 814)),
    ((3047, 3052), (815, 815)),
    ((3053, 3053), (816, 816)),
    ((3054, 3054), (817, 817)),
    ((3055, 3055), (818, 818)),
    ((3056, 3056), (819, 819)),
    ((3057, 3057), (820, 820)),
    ((3070, 3074), (823, 823)),
    ((3076, 3081), (825, 825)),
    ((3082, 3087), (826, 826)),
    ((3088, 3093), (827, 827)),
    ((3094, 3099), (828, 828)),
    ((3100, 3105), (829, 829)),
    ((3106, 3111), (830, 830)),
    ((3112, 3112), (831, 831)),
    ((3113, 3113), (832, 832)),
    ((3114, 3114), (833, 833)),
    ((3115, 3115), (834, 834)),
    ((3116, 3116), (835, 835)),
    ((3129, 3133), (838, 838)),
    ((3135, 3140), (840, 840)),
    ((3141, 3146), (841, 841)),
    ((3147, 3152), (842, 842)),
    ((3153, 3158), (843, 843)),
    ((3159, 3164), (844, 844)),
    ((3165, 3170), (845, 845)),
    ((3171, 3171), (846, 846)),
    ((3172, 3172), (847, 847)),
    ((3173, 3173), (848, 848)),
    ((3174, 3174), (849, 849)),
    ((3175, 3175), (850, 850)),
    ((3188, 3192), (854, 854)),
    ((3194, 3199), (856, 856)),
    ((3200, 3205), (857, 857)),
    ((3206, 3211), (858, 858)),
    ((3212, 3217), (859, 859)),
    ((3218, 3223), (860, 860)),
    ((3224, 3229), (861, 861)),
    ((3230, 3230), (862, 862)),
    ((3231, 3231), (863, 863)),
    ((3232, 3232), (864, 864)),
    ((3233, 3233), (865, 865)),
    ((3234, 3234), (866, 866)),
    ((3247, 3251), (869, 869)),
    ((3253, 3258), (871, 871)),
    ((3259, 3264), (872, 872)),
    ((3265, 3270), (873, 873)),
    ((3271, 3276), (874, 874)),
    ((3277, 3282), (875, 875)),
    ((3283, 3288), (876, 876)),
    ((3289, 3289), (877, 877)),
    ((3290, 3290), (878, 878)),
    ((3291, 3291), (879, 879)),
    ((3292, 3292), (880, 880)),
    ((3293, 3293), (881, 881)),
    ((3306, 3310), (885, 885)),
    ((3312, 3317), (887, 887)),
    ((3318, 3323), (888, 888)),
    ((3324, 3329), (889, 889)),
    ((3330, 3335), (890, 890)),
    ((3336, 3341), (891, 891)),
    ((3342, 3347), (892, 892)),
    ((3348, 3348), (893, 893)),
    ((3349, 3349), (894, 894)),
    ((3350, 3350), (895, 895)),
    ((3351, 3351), (896, 896)),
    ((3352, 3352), (897, 897)),
    ((3365, 3369), (900, 900)),
    ((3371, 3376), (902, 902)),
    ((3377, 3382), (903, 903)),
    ((3383, 3388), (904, 904)),
    ((3389, 3394), (905, 905)),
    ((3395, 3400), (906, 906)),
    ((3401, 3406), (907, 907)),
    ((3407, 3407), (908, 908)),
    ((3408, 3408), (909, 909)),
    ((3409, 3409), (910, 910)),
    ((3410, 3410), (911, 911)),
    ((3411, 3411), (912, 912)),
    ((3424, 3428), (915, 915)),
    ((3430, 3435), (917, 917)),
    ((3436, 3441), (918, 918)),
    ((3442, 3447), (919, 919)),
    ((3448, 3453), (920, 920)),
    ((3454, 3459), (921, 921)),
    ((3460, 3465), (922, 922)),
    ((3466, 3466), (923, 923)),
    ((3467, 3467), (924, 924)),
    ((3468, 3468), (925, 925)),
    ((3469, 3469), (926, 926)),
    ((3470, 3470), (927, 927)),
    ((3483, 3487), (931, 931)),
    ((3489, 3494), (933, 933)),
    ((3495, 3500), (934, 934)),
    ((3501, 3506), (935, 935)),
    ((3507, 3512), (936, 936)),
    ((3513, 3518), (937, 937)),
    ((3519, 3524), (938, 938)),
    ((3525, 3525), (939, 939)),
    ((3526, 3526), (940, 940)),
    ((3527, 3527), (941, 941)),
    ((3528, 3528), (942, 942)),
    ((3529, 3529), (943, 943)),
    ((3542, 3546), (951, 951)),
    ((3548, 3553), (953, 953)),
    ((3554, 3559), (954, 954)),
    ((3560, 3565), (955, 955)),
    ((3566, 3571), (956, 956)),
    ((3572, 3577), (957, 957)),
    ((3578, 3583), (958, 958)),
    ((3584, 3584), (959, 959)),
    ((3585, 3585), (960, 960)),
    ((3586, 3586), (961, 961)),
    ((3587, 3587), (962, 962)),
    ((3588, 3588), (963, 963)),
    ((3601, 3605), (966, 966)),
    ((3607, 3612), (968, 968)),
    ((3613, 3618), (969, 969)),
    ((3619, 3624), (970, 970)),
    ((3625, 3630), (971, 971)),
    ((3631, 3636), (972, 972)),
    ((3637, 3642), (973, 973)),
    ((3643, 3643), (974, 974)),
    ((3644, 3644), (975, 975)),
    ((3645, 3645), (976, 976)),
    ((3646, 3646), (977, 977)),
    ((3647, 3647), (978, 978)),
    ((3660, 3664), (982, 982)),
    ((3666, 3671), (984, 984)),
    ((3672, 3677), (985, 985)),
    ((3678, 3683), (986, 986)),
    ((3684, 3689), (987, 987)),
    ((3690, 3695), (988, 988)),
    ((3696, 3701), (989, 989)),
    ((3702, 3702), (990, 990)),
    ((3703, 3703), (991, 991)),
    ((3704, 3704), (992, 992)),
    ((3705, 3705), (993, 993)),
    ((3706, 3706), (994, 994)),
    ((3719, 3723), (998, 998)),
    ((3725, 3730), (1000, 1000)),
    ((3731, 3736), (1001, 1001)),
    ((3737, 3742), (1002, 1002)),
    ((3743, 3748), (1003, 1003)),
    ((3749, 3754), (1004, 1004)),
    ((3755, 3760), (1005, 1005)),
    ((3761, 3761), (1006, 1006)),
    ((3762, 3762), (1007, 1007)),
    ((3763, 3763), (1008, 1008)),
    ((3764, 3764), (1009, 1009)),
    ((3765, 3765), (1010, 1010)),
    ((3778, 3782), (1013, 1013)),
    ((3784, 3789), (1015, 1015)),
    ((3790, 3795), (1016, 1016)),
    ((3796, 3801), (1017, 1017)),
    ((3802, 3807), (1018, 1018)),
    ((3808, 3813), (1019, 1019)),
    ((3814, 3819), (1020, 1020)),
    ((3820, 3820), (1021, 1021)),
    ((3821, 3821), (1022, 1022)),
    ((3822, 3822), (1023, 1023)),
    ((3823, 3823), (1024, 1024)),
    ((3824, 3824), (1025, 1025)),
    ((3837, 3841), (1028, 1028)),
    ((3843, 3848), (1030, 1030)),
    ((3849, 3854), (1031, 1031)),
    ((3855, 3860), (1032, 1032)),
    ((3861, 3866), (1033, 1033)),
    ((3867, 3872), (1034, 1034)),
    ((3873, 3878), (1035, 1035)),
    ((3879, 3879), (1036, 1036)),
    ((3880, 3880), (1037, 1037)),
    ((3881, 3881), (1038, 1038)),
    ((3882, 3882), (1039, 1039)),
    ((3883, 3883), (1040, 1040)),
    ((3896, 3900), (1044, 1044)),
    ((3902, 3907), (1046, 1046)),
    ((3908, 3913), (1047, 1047)),
    ((3914, 3919), (1048, 1048)),
    ((3920, 3925), (1049, 1049)),
    ((3926, 3931), (1050, 1050)),
    ((3932, 3937), (1051, 1051)),
    ((3938, 3938), (1052, 1052)),
    ((3939, 3939), (1053, 1053)),
    ((3940, 3940), (1054, 1054)),
    ((3941, 3941), (1055, 1055)),
    ((3942, 3942), (1056, 1056)),
    ((3955, 3959), (1059, 1059)),
    ((3961, 3966), (1061, 1061)),
    ((3967, 3972), (1062, 1062)),
    ((3973, 3978), (1063, 1063)),
    ((3979, 3984), (1064, 1064)),
    ((3985, 3990), (1065, 1065)),
    ((3991, 3996), (1066, 1066)),
    ((3997, 3997), (1067, 1067)),
    ((3998, 3998), (1068, 1068)),
    ((3999, 3999), (1069, 1069)),
    ((4000, 4000), (1070, 1070)),
    ((4001, 4001), (1071, 1071)),
    ((4014, 4018), (1075, 1075)),
    ((4020, 4025), (1077, 1077)),
    ((4026, 4031), (1078, 1078)),
    ((4032, 4037), (1079, 1079)),
    ((4038, 4043), (1080, 1080)),
    ((4044, 4049), (1081, 1081)),
    ((4050, 4055), (1082, 1082)),
    ((4056, 4056), (1083, 1083)),
    ((4057, 4057), (1084, 1084)),
    ((4058, 4058), (1085, 1085)),
    ((4059, 4059), (1086, 1086)),
    ((4060, 4060), (1087, 1087)),
    ((4073, 4077), (1090, 1090)),
    ((4079, 4084), (1092, 1092)),
    ((4085, 4090), (1093, 1093)),
    ((4091, 4096), (1094, 1094)),
    ((4097, 4102), (1095, 1095)),
    ((4103, 4108), (1096, 1096)),
    ((4109, 4114), (1097, 1097)),
    ((4115, 4115), (1098, 1098)),
    ((4116, 4116), (1099, 1099)),
    ((4117, 4117), (1100, 1100)),
    ((4118, 4118), (1101, 1101)),
    ((4119, 4119), (1102, 1102)),
    ((4132, 4136), (1105, 1105)),
    ((4138, 4143), (1107, 1107)),
    ((4144, 4149), (1108, 1108)),
    ((4150, 4155), (1109, 1109)),
    ((4156, 4161), (1110, 1110)),
    ((4162, 4167), (1111, 1111)),
    ((4168, 4173), (1112, 1112)),
    ((4174, 4174), (1113, 1113)),
    ((4175, 4175), (1114, 1114)),
    ((4176, 4176), (1115, 1115)),
    ((4177, 4177), (1116, 1116)),
    ((4178, 4178), (1117, 1117)),
    ((4191, 4195), (1121, 1121)),
    ((4197, 4202), (1123, 1123)),
    ((4203, 4208), (1124, 1124)),
    ((4209, 4214), (1125, 1125)),
    ((4215, 4220), (1126, 1126)),
    ((4221, 4226), (1127, 1127)),
    ((4227, 4232), (1128, 1128)),
    ((4233, 4233), (1129, 1129)),
    ((4234, 4234), (1130, 1130)),
    ((4235, 4235), (1131, 1131)),
    ((4236, 4236), (1132, 1132)),
    ((4237, 4237), (1133, 1133)),
    ((4250, 4254), (1143, 1143)),
    ((4256, 4261), (1145, 1145)),
    ((4262, 4267), (1146, 1146)),
    ((4268, 4273), (1147, 1147)),
    ((4274, 4279), (1148, 1148)),
    ((4280, 4285), (1149, 1149)),
    ((4286, 4291), (1150, 1150)),
    ((4292, 4292), (1151, 1151)),
    ((4293, 4293), (1152, 1152)),
    ((4294, 4294), (1153, 1153)),
    ((4295, 4295), (1154, 1154)),
    ((4296, 4296), (1155, 1155)),
    ((4309, 4313), (1158, 1158)),
    ((4315, 4320), (1160, 1160)),
    ((4321, 4326), (1161, 1161)),
    ((4327, 4332), (1162, 1162)),
    ((4333, 4338), (1163, 1163)),
    ((4339, 4344), (1164, 1164)),
    ((4345, 4350), (1165, 1165)),
    ((4351, 4351), (1166, 1166)),
    ((4352, 4352), (1167, 1167)),
    ((4353, 4353), (1168, 1168)),
    ((4354, 4354), (1169, 1169)),
    ((4355, 4355), (1170, 1170)),
    ((4368, 4372), (1174, 1174)),
    ((4374, 4379), (1176, 1176)),
    ((4380, 4385), (1177, 1177)),
    ((4386, 4391), (1178, 1178)),
    ((4392, 4397), (1179, 1179)),
    ((4398, 4403), (1180, 1180)),
    ((4404, 4409), (1181, 1181)),
    ((4410, 4410), (1182, 1182)),
    ((4411, 4411), (1183, 1183)),
    ((4412, 4412), (1184, 1184)),
    ((4413, 4413), (1185, 1185)),
    ((4414, 4414), (1186, 1186)),
    ((4427, 4431), (1190, 1190)),
    ((4433, 4438), (1192, 1192)),
    ((4439, 4444), (1193, 1193)),
    ((4445, 4450), (1194, 1194)),
    ((4451, 4456), (1195, 1195)),
    ((4457, 4462), (1196, 1196)),
    ((4463, 4468), (1197, 1197)),
    ((4469, 4469), (1198, 1198)),
    ((4470, 4470), (1199, 1199)),
    ((4471, 4471), (1200, 1200)),
    ((4472, 4472), (1201, 1201)),
    ((4473, 4473), (1202, 1202)),
    ((4486, 4490), (1205, 1205)),
    ((4492, 4497), (1207, 1207)),
    ((4498, 4503), (1208, 1208)),
    ((4504, 4509), (1209, 1209)),
    ((4510, 4515), (1210, 1210)),
    ((4516, 4521), (1211, 1211)),
    ((4522, 4527), (1212, 1212)),
    ((4528, 4528), (1213, 1213)),
    ((4529, 4529), (1214, 1214)),
    ((4530, 4530), (1215, 1215)),
    ((4531, 4531), (1216, 1216)),
    ((4532, 4532), (1217, 1217)),
    ((4545, 4549), (1220, 1220)),
    ((4551, 4556), (1222, 1222)),
    ((4557, 4562), (1223, 1223)),
    ((4563, 4568), (1224, 1224)),
    ((4569, 4574), (1225, 1225)),
    ((4575, 4580), (1226, 1226)),
    ((4581, 4586), (1227, 1227)),
    ((4587, 4587), (1228, 1228)),
    ((4588, 4588), (1229, 1229)),
    ((4589, 4589), (1230, 1230)),
    ((4590, 4590), (1231, 1231)),
    ((4591, 4591), (1232, 1232)),
    ((4604, 4608), (1237, 1237)),
    ((4610, 4615), (1239, 1239)),
    ((4616, 4621), (1240, 1240)),
    ((4622, 4627), (1241, 1241)),
    ((4628, 4633), (1242, 1242)),
    ((4634, 4639), (1243, 1243)),
    ((4640, 4645), (1244, 1244)),
    ((4646, 4646), (1245, 1245)),
    ((4647, 4647), (1246, 1246)),
    ((4648, 4648), (1247, 1247)),
    ((4649, 4649), (1248, 1248)),
    ((4650, 4650), (1249, 1249)),
    ((4663, 4667), (1252, 1252)),
    ((4669, 4674), (1254, 1254)),
    ((4675, 4680), (1255, 1255)),
    ((4681, 4686), (1256, 1256)),
    ((4687, 4692), (1257, 1257)),
    ((4693, 4698), (1258, 1258)),
    ((4699, 4704), (1259, 1259)),
    ((4705, 4705), (1260, 1260)),
    ((4706, 4706), (1261, 1261)),
    ((4707, 4707), (1262, 1262)),
    ((4708, 4708), (1263, 1263)),
    ((4709, 4709), (1264, 1264)),
    ((4722, 4726), (1268, 1268)),
    ((4728, 4733), (1270, 1270)),
    ((4734, 4739), (1271, 1271)),
    ((4740, 4745), (1272, 1272)),
    ((4746, 4751), (1273, 1273)),
    ((4752, 4757), (1274, 1274)),
    ((4758, 4763), (1275, 1275)),
    ((4764, 4764), (1276, 1276)),
    ((4765, 4765), (1277, 1277)),
    ((4766, 4766), (1278, 1278)),
    ((4767, 4767), (1279, 1279)),
    ((4768, 4768), (1280, 1280)),
    ((4781, 4785), (1283, 1283)),
    ((4787, 4792), (1285, 1285)),
    ((4793, 4798), (1286, 1286)),
    ((4799, 4804), (1287, 1287)),
    ((4805, 4810), (1288, 1288)),
    ((4811, 4816), (1289, 1289)),
    ((4817, 4822), (1290, 1290)),
    ((4823, 4823), (1291, 1291)),
    ((4824, 4824), (1292, 1292)),
    ((4825, 4825), (1293, 1293)),
    ((4826, 4826), (1294, 1294)),
    ((4827, 4827), (1295, 1295)),
    ((4840, 4844), (1298, 1298)),
    ((4846, 4851), (1300, 1300)),
    ((4852, 4857), (1301, 1301)),
    ((4858, 4863), (1302, 1302)),
    ((4864, 4869), (1303, 1303)),
    ((4870, 4875), (1304, 1304)),
    ((4876, 4881), (1305, 1305)),
    ((4882, 4882), (1306, 1306)),
    ((4883, 4883), (1307, 1307)),
    ((4884, 4884), (1308, 1308)),
    ((4885, 4885), (1309, 1309)),
    ((4886, 4886), (1310, 1310)),
    ((4899, 4903), (1314, 1314)),
    ((4905, 4910), (1316, 1316)),
    ((4911, 4916), (1317, 1317)),
    ((4917, 4922), (1318, 1318)),
    ((4923, 4928), (1319, 1319)),
    ((4929, 4934), (1320, 1320)),
    ((4935, 4940), (1321, 1321)),
    ((4941, 4941), (1322, 1322)),
    ((4942, 4942), (1323, 1323)),
    ((4943, 4943), (1324, 1324)),
    ((4944, 4944), (1325, 1325)),
    ((4945, 4945), (1326, 1326)),
    ((4958, 4962), (1333, 1333)),
    ((4964, 4969), (1335, 1335)),
    ((4970, 4975), (1336, 1336)),
    ((4976, 4981), (1337, 1337)),
    ((4982, 4987), (1338, 1338)),
    ((4988, 4993), (1339, 1339)),
    ((4994, 4999), (1340, 1340)),
    ((5000, 5000), (1341, 1341)),
    ((5001, 5001), (1342, 1342)),
    ((5002, 5002), (1343, 1343)),
    ((5003, 5003), (1344, 1344)),
    ((5004, 5004), (1345, 1345)),
    ((5017, 5021), (1348, 1348)),
    ((5023, 5028), (1350, 1350)),
    ((5029, 5034), (1351, 1351)),
    ((5035, 5040), (1352, 1352)),
    ((5041, 5046), (1353, 1353)),
    ((5047, 5052), (1354, 1354)),
    ((5053, 5058), (1355, 1355)),
    ((5059, 5059), (1356, 1356)),
    ((5060, 5060), (1357, 1357)),
    ((5061, 5061), (1358, 1358)),
    ((5062, 5062), (1359, 1359)),
    ((5063, 5063), (1360, 1360)),
    ((5076, 5080), (1364, 1364)),
    ((5082, 5087), (1366, 1366)),
    ((5088, 5093), (1367, 1367)),
    ((5094, 5099), (1368, 1368)),
    ((5100, 5105), (1369, 1369)),
    ((5106, 5111), (1370, 1370)),
    ((5112, 5117), (1371, 1371)),
    ((5118, 5118), (1372, 1372)),
    ((5119, 5119), (1373, 1373)),
    ((5120, 5120), (1374, 1374)),
    ((5121, 5121), (1375, 1375)),
    ((5122, 5122), (1376, 1376)),
    ((5135, 5139), (1380, 1380)),
    ((5141, 5146), (1382, 1382)),
    ((5147, 5152), (1383, 1383)),
    ((5153, 5158), (1384, 1384)),
    ((5159, 5164), (1385, 1385)),
    ((5165, 5170), (1386, 1386)),
    ((5171, 5176), (1387, 1387)),
    ((5177, 5177), (1388, 1388)),
    ((5178, 5178), (1389, 1389)),
    ((5179, 5179), (1390, 1390)),
    ((5180, 5180), (1391, 1391)),
    ((5181, 5181), (1392, 1392)),
    ((5194, 5198), (1395, 1395)),
    ((5200, 5205), (1397, 1397)),
    ((5206, 5211), (1398, 1398)),
    ((5212, 5217), (1399, 1399)),
    ((5218, 5223), (1400, 1400)),
    ((5224, 5229), (1401, 1401)),
    ((5230, 5235), (1402, 1402)),
    ((5236, 5236), (1403, 1403)),
    ((5237, 5237), (1404, 1404)),
    ((5238, 5238), (1405, 1405)),
    ((5239, 5239), (1406, 1406)),
    ((5240, 5240), (1407, 1407)),
    ((5253, 5257), (1410, 1410)),
    ((5259, 5264), (1412, 1412)),
    ((5265, 5270), (1413, 1413)),
    ((5271, 5276), (1414, 1414)),
    ((5277, 5282), (1415, 1415)),
    ((5283, 5288), (1416, 1416)),
    ((5289, 5294), (1417, 1417)),
    ((5295, 5295), (1418, 1418)),
    ((5296, 5296), (1419, 1419)),
    ((5297, 5297), (1420, 1420)),
    ((5298, 5298), (1421, 1421)),
    ((5299, 5299), (1422, 1422)),
    ((5312, 5316), (1427, 1427)),
    ((5318, 5323), (1429, 1429)),
    ((5324, 5329), (1430, 1430)),
    ((5330, 5335), (1431, 1431)),
    ((5336, 5341), (1432, 1432)),
    ((5342, 5347), (1433, 1433)),
    ((5348, 5353), (1434, 1434)),
    ((5354, 5354), (1435, 1435)),
    ((5355, 5355), (1436, 1436)),
    ((5356, 5356), (1437, 1437)),
    ((5357, 5357), (1438, 1438)),
    ((5358, 5358), (1439, 1439)),
    ((5371, 5375), (1442, 1442)),
    ((5377, 5382), (1444, 1444)),
    ((5383, 5388), (1445, 1445)),
    ((5389, 5394), (1446, 1446)),
    ((5395, 5400), (1447, 1447)),
    ((5401, 5406), (1448, 1448)),
    ((5407, 5412), (1449, 1449)),
    ((5413, 5413), (1450, 1450)),
    ((5414, 5414), (1451, 1451)),
    ((5415, 5415), (1452, 1452)),
    ((5416, 5416), (1453, 1453)),
    ((5417, 5417), (1454, 1454)),
    ((5430, 5434), (1458, 1458)),
    ((5436, 5441), (1460, 1460)),
    ((5442, 5447), (1461, 1461)),
    ((5448, 5453), (1462, 1462)),
    ((5454, 5459), (1463, 1463)),
    ((5460, 5465), (1464, 1464)),
    ((5466, 5471), (1465, 1465)),
    ((5472, 5472), (1466, 1466)),
    ((5473, 5473), (1467, 1467)),
    ((5474, 5474), (1468, 1468)),
    ((5475, 5475), (1469, 1469)),
    ((5476, 5476), (1470, 1470)),
    ((5489, 5493), (1473, 1473)),
    ((5495, 5500), (1475, 1475)),
    ((5501, 5506), (1476, 1476)),
    ((5507, 5512), (1477, 1477)),
    ((5513, 5518), (1478, 1478)),
    ((5519, 5524), (1479, 1479)),
    ((5525, 5530), (1480, 1480)),
    ((5531, 5531), (1481, 1481)),
    ((5532, 5532), (1482, 1482)),
    ((5533, 5533), (1483, 1483)),
    ((5534, 5534), (1484, 1484)),
    ((5535, 5535), (1485, 1485)),
    ((5548, 5552), (1488, 1488)),
    ((5554, 5559), (1490, 1490)),
    ((5560, 5565), (1491, 1491)),
    ((5566, 5571), (1492, 1492)),
    ((5572, 5577), (1493, 1493)),
    ((5578, 5583), (1494, 1494)),
    ((5584, 5589), (1495, 1495)),
    ((5590, 5590), (1496, 1496)),
    ((5591, 5591), (1497, 1497)),
    ((5592, 5592), (1498, 1498)),
    ((5593, 5593), (1499, 1499)),
    ((5594, 5594), (1500, 1500)),
    ((5607, 5611), (1504, 1504)),
    ((5613, 5618), (1506, 1506)),
    ((5619, 5624), (1507, 1507)),
    ((5625, 5630), (1508, 1508)),
    ((5631, 5636), (1509, 1509)),
    ((5637, 5642), (1510, 1510)),
    ((5643, 5648), (1511, 1511)),
    ((5649, 5649), (1512, 1512)),
    ((5650, 5650), (1513, 1513)),
    ((5651, 5651), (1514, 1514)),
    ((5652, 5652), (1515, 1515)),
    ((5653, 5653), (1516, 1516)),
)
