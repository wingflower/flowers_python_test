SELECT * FROM information_schema.columns
WHERE 	  table_schema = 'public'
AND 	  table_name = 'table99';

SELECT 	  column_name
	, data_type 
	, (CASE 
		WHEN data_type = 'bigint' THEN numeric_precision
		WHEN data_type = 'timestamp without time zone' THEN datetime_precision
		WHEN data_type = 'numeric' THEN numeric_precision_radix
		ELSE character_maximum_length
	  END) AS data_length
	, CASE WHEN column_name = (		
		SELECT column_name 
		FROM information_schema.key_column_usage kc 
		WHERE table_name = 'table99'
		) THEN 1 ELSE 0 END AS is_primary_key
FROM 	  information_schema.columns
WHERE 	  table_schema = 'public'
AND 	  table_name = 'table99';
