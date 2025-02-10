SELECT
	@i := @i + 1 AS id
FROM
	( SELECT @i := -1 UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 ) t1,
	( SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 ) t2,
	( SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 ) t3,
	( SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 ) t4,
	( SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 ) t5,
	( SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 ) t6,
	( SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 ) t7;


SELECT *
FROM blue_army_article_stage
-- WHERE article_id in ("live@7203264950649867009_1677140865057","live_audioslice@7203264950649867009_1677140875563")
WHERE find_in_set(article_id, 'live@7188036505758108422_1673599808793,live_audioslice@7188036505758108422_1673599959876')
limit 10;

select ar.* from (select substring_index(
                                 substring_index(T.article_ids, ',', topic.help_topic_id + 1), ',', -1
                             ) as tag
                  from blue_army_article_batch T
                           join (SELECT @i := @i + 1 AS help_topic_id
                                 FROM (SELECT @i := -1 UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) t1,
                                      (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) t2,
                                      (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) t3,
                                      (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) t4,
                                      (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) t5,
                                      (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) t6,
                                      (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) t7) topic
                                on topic.help_topic_id <
                                   (length(T.article_ids) - length(replace(T.article_ids, ',', '')) + 1)
                  where id = 2
                  ) tb_ar_ids join blue_army_article ar on tb_ar_ids.tag = ar.article_id;


