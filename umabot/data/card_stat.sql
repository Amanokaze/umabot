select `card`.`id` `card_id`,
	   `card`.`chara_id` `chara_id`,
	   `crd`.`rarity` `rarity`,
	   `crd`.`speed` `speed`,
	   `crd`.`stamina` `stamina`,
	   `crd`.`pow` `pow`,
	   `crd`.`guts` `guts`,
	   `crd`.`wiz` `wiz`,
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
   and `crd`.`rarity` > 0
   and `crd`.`card_id` = ?
 order by `crd`.`rarity` asc