def appendix_a_validate(ds, appendix_a_dict, coord)


    for global_att_name in possible_global_atts:
        print(global_att_name)
        global_att = ds.getncattr(global_att_name)
        att_dict = hier_dict[global_att_name]
        att_loc = att_dict['attr_loc']
        if 'G' not in att_loc:
            print("Attribute {} should not be in Global attributes. "
                  "Valid location(s) are [{}]".format(global_att,
                                                      ', '.join(att_loc)))
        else:
            print(handle_dtype_check(global_att, att_dict))
