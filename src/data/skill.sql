SELECT `sd`.`id` AS `skill_id`
     , `sd`.`rarity` AS `rarity`
     , `sd`.`group_id` AS `group_id`
     , `sd`.`skill_category` AS `skill_category`
     , `sd`.`condition_1` AS `condition_1`
     , `sd`.`condition_2` AS `condition_2`
     , `td_name`.`text` AS `skill_name`
     , `td_desc`.`text` AS `skill_desc`
FROM ((`skill_data` `sd`
    JOIN `text_data` `td_name`
        ON (`sd`.`id` = `td_name`.`index`))
    JOIN `text_data` `td_desc`
        ON (`sd`.`id` = `td_desc`.`index`))
WHERE `td_name`.`category` = 47
    AND `td_desc`.`category` = 48
	and `td_name`.`text` like ?
