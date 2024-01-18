SELECT `sd`.`id` AS `skill_id`
     , `sd`.`precondition_1` AS `precondition_1`
     , `sd`.`condition_1` AS `condition_1`
     , `sd`.`precondition_2` AS `precondition_2`
     , `sd`.`condition_2` AS `condition_2`
FROM `skill_data` `sd`
WHERE `sd`.`id` = ?     
