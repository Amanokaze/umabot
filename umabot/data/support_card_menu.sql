select `scd`.`id` scd_id,
	   `scd`.`chara_id` chara_id,
	   `scd`.`rarity` rarity,
	   `scd`.`support_card_type` support_card_type,
	   `scd`.`command_id` command_id,
	   `smhg`.`icon_id` hint_icon_id,
	   `td_sc`.`text` sc_name,
	   `td_chara`.`text` chara_name
  from (((`support_card_data` `scd`
    JOIN `chara_data` `cd`
	  ON (`scd`.`chara_id` = `cd`.`id`))
    JOIN `text_data` `td_chara`
	  ON (`td_chara`.`index` = `scd`.`chara_id`))
	JOIN `text_data` `td_sc`
	  ON (`td_sc`.`index` = `scd`.`id`))
	LEFT JOIN (select `smhg`.`support_card_id`, 
					  `smhg`.`hint_id`, 
				  	  `sd`.`icon_id`
				 from `single_mode_hint_gain` `smhg`
			     join `skill_data` `sd`
				   on (`smhg`.`hint_value_1` = `sd`.`id`)
				where `smhg`.`support_card_id` = ? limit 1
			  ) `smhg`
	  ON (`scd`.`id` = `smhg`.`support_card_id` and `scd`.`skill_set_id` = `smhg`.`hint_id`)
 where `td_sc`.`category` = 76
   and `td_chara`.`category` = 6
   and `scd`.`id` = ?