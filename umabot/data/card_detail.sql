select `card`.`id` `card_id`,
	   `card`.`chara_id` `chara_id`,
	   `card`.`available_skill_set_id` `available_skill_set_id`,
	   `crd`.`skill_set` `skill_set`,
	   `td_card`.`text` `card_name`,
	   `td_chara`.`text` `chara_name`
  from (((`card_data` `card`
    JOIN `text_data` `td_chara`
	  ON (`td_chara`.`index` = `card`.`chara_id`))
	JOIN `text_data` `td_card`
	  ON (`td_card`.`index` = `card`.`id`))
	LEFT JOIN `card_rarity_data` `crd`
	  ON (`card`.`id` = `crd`.`card_id`))
 where `td_card`.`category` = 5
   and `td_chara`.`category` = 6
   and `crd`.`rarity` = 3
   and `card`.`id` = ?
