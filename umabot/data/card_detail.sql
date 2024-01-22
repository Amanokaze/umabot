select `card`.`id` `card_id`,
	   `card`.`chara_id` `chara_id`,
	   `card`.`available_skill_set_id` `available_skill_set_id`,
	   `crd`.`skill_set` `skill_set`,
	   `crd`.`speed` `speed`,
	   `crd`.`stamina` `stamina`,
	   `crd`.`pow` `pow`,
	   `crd`.`guts` `guts`,
	   `crd`.`wiz` `wiz`,
	   `td_card`.`text` `card_name`,
	   `td_chara`.`text` `chara_name`,
	   `td_skill`.`skill_id1` `unique_skill_id`,	   
	   `td_skill`.`text` `unique_skill_name`,
	   `td_skill`.`icon_id` `unique_skill_icon_id`
  from ((((`card_data` `card`
    JOIN `text_data` `td_chara`
	  ON (`td_chara`.`index` = `card`.`chara_id`))
	JOIN `text_data` `td_card`
	  ON (`td_card`.`index` = `card`.`id`))
	LEFT JOIN `card_rarity_data` `crd`
	  ON (`card`.`id` = `crd`.`card_id`))
	LEFT JOIN (select `ss`.`id`, `sd`.`icon_id`, `ss`.`skill_id1`, `td_skill`.`text` 
				 from `skill_set` `ss`
				    , `skill_data` `sd`
					, `text_data` `td_skill`
				 where `ss`.`skill_id1` = `sd`.`id`
				   and `td_skill`.`index` = `sd`.`id`
				   and `td_skill`.`category` = 47) `td_skill`
	  ON (`crd`.`skill_set` = `td_skill`.`id`))
 where `td_card`.`category` = 5
   and `td_chara`.`category` = 6
   and `crd`.`rarity` = 3
   and `card`.`id` = ?
