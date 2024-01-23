select `card`.`id` `card_id`,
	   `card`.`chara_id` `chara_id`,
	   `crd`.`rarity` `rarity`,
	   `crd`.`speed` `speed`,
	   `crd`.`stamina` `stamina`,
	   `crd`.`pow` `pow`,
	   `crd`.`guts` `guts`,
	   `crd`.`wiz` `wiz`,
	   `crd`.`proper_distance_short` `proper_distance_short`,
	   `crd`.`proper_distance_mile` `proper_distance_mile`,
	   `crd`.`proper_distance_middle` `proper_distance_middle`,
	   `crd`.`proper_distance_long` `proper_distance_long`,
	   `crd`.`proper_running_style_nige` `proper_running_style_nige`,
	   `crd`.`proper_running_style_senko` `proper_running_style_senko`,
	   `crd`.`proper_running_style_sashi` `proper_running_style_sashi`,
	   `crd`.`proper_running_style_oikomi` `proper_running_style_oikomi`,
	   `crd`.`proper_ground_turf` `proper_ground_turf`,
	   `crd`.`proper_ground_dirt` `proper_ground_dirt`,
	   `card`.`talent_speed` `talent_speed`,
	   `card`.`talent_stamina` `talent_stamina`,
	   `card`.`talent_pow` `talent_pow`,
	   `card`.`talent_guts` `talent_guts`,
	   `card`.`talent_wiz` `talent_wiz`,
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