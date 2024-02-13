select `sd`.`id` `skill_id`,
	   `sd`.`skill_category` `skill_category`,
	   `sd`.`icon_id` `hint_icon_id`,
	   `td_name`.`text` `skill_name`,
	   `td_desc`.`text` `skill_desc`
  from (((`single_mode_hint_gain` `smhg`
  join `skill_data` `sd`
    on (`smhg`.`hint_value_1` = `sd`.`id`))
  join `text_data` `td_name`
    on (`td_name`.`index` = `sd`.`id` and `td_name`.`category`=47))
  join `text_data` `td_desc`
    on (`td_desc`.`index` = `sd`.`id` and `td_desc`.`category`=48))
 where `smhg`.`support_card_id` = ?
   and `smhg`.`hint_gain_type` = 0
 order by `sd`.`skill_category` asc