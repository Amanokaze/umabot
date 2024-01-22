SELECT `sd`.`id` AS `skill_id`
     , `sd`.`group_id` AS `group_id`
     , `sd`.`icon_id` AS `icon_id`
     , `sd`.`precondition_1` AS `precondition_1`
     , `sd`.`condition_1` AS `condition_1`
     , `sd`.`ability_type_1_1` AS `ability_type_1_1`
     , `sd`.`ability_type_1_2` AS `ability_type_1_2`
     , `sd`.`ability_type_1_3` AS `ability_type_1_3`
     , `sd`.`float_ability_time_1` AS `float_ability_time_1`
     , `sd`.`float_cooldown_time_1` AS `float_cooldown_time_1`
     , `sd`.`float_ability_value_1_1` AS `float_ability_value_1_1`
     , `sd`.`float_ability_value_1_2` AS `float_ability_value_1_2`
     , `sd`.`float_ability_value_1_3` AS `float_ability_value_1_3`
     , `sd`.`precondition_2` AS `precondition_2`
     , `sd`.`condition_2` AS `condition_2`
     , `sd`.`ability_type_2_1` AS `ability_type_2_1`
     , `sd`.`ability_type_2_2` AS `ability_type_2_2`
     , `sd`.`ability_type_2_3` AS `ability_type_2_3`
     , `sd`.`float_ability_time_2` AS `float_ability_time_2`
     , `sd`.`float_cooldown_time_2` AS `float_cooldown_time_2`
     , `sd`.`float_ability_value_2_1` AS `float_ability_value_2_1`
     , `sd`.`float_ability_value_2_2` AS `float_ability_value_2_2`
     , `sd`.`float_ability_value_2_3` AS `float_ability_value_2_3`
	 , `smsnp`.`need_skill_point` AS `need_skill_point`
	 , `ass`.`need_rank` AS `need_rank`
     , `td_name`.`text` AS `skill_name`
     , `td_desc`.`text` AS `skill_desc`
FROM ((((`skill_data` `sd`
    JOIN `text_data` `td_name`
        ON (`sd`.`id` = `td_name`.`index`))
    JOIN `text_data` `td_desc`
        ON (`sd`.`id` = `td_desc`.`index`))
	LEFT JOIN `single_mode_skill_need_point` `smsnp`
		ON (`sd`.`id` = `smsnp`.`id`))
    LEFT JOIN `available_skill_set` `ass`
        ON (`sd`.`id` = `ass`.`skill_id`))
WHERE `td_name`.`category` = 47
    AND `td_desc`.`category` = 48
    and `ass`.`available_skill_set_id` = ?
	and `ass`.`need_rank` > 0

