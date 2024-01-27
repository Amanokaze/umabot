select `scd`.`id` scd_id,
	   `scd`.`chara_id` chara_id,
	   date(`scd`.`start_date`, 'unixepoch','localtime') `start_date`,
	   `scd`.`rarity` rarity,
	   `td_sc`.`text` sc_name,
	   `td_chara`.`text` chara_name
  from (((`support_card_data` `scd`
    JOIN `chara_data` `cd`
	  ON (`scd`.`chara_id` = `cd`.`id`))
    JOIN `text_data` `td_chara`
	  ON (`td_chara`.`index` = `scd`.`chara_id`))
	JOIN `text_data` `td_sc`
	  ON (`td_sc`.`index` = `scd`.`id`))
 where `td_sc`.`category` = 76
   and `td_chara`.`category` = 6
   and (`td_sc`.`text` like ? or `td_chara`.`text` like ?)
 order by `scd`.`rarity` desc, `scd`.`start_date`;