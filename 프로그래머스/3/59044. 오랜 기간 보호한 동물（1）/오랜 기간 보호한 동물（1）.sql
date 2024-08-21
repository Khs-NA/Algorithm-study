SELECT * FROM (
    SELECT
        i.NAME,
        i.DATETIME
    FROM
        ANIMAL_INS i
    LEFT JOIN
        ANIMAL_OUTS o
    ON
        i.ANIMAL_ID = o.ANIMAL_ID
    WHERE
        o.ANIMAL_ID IS NULL
    ORDER BY
        i.DATETIME
)
WHERE ROWNUM <= 3;
