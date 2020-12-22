SELECT
    m.date,
    m.tobs,
    s.station
FROM
    measurement m
JOIN station s on m.station = s.station
WHERE
    date >= (
                SELECT
                    date(MAX(date), '-365 day')
                FROM
                    measurement
                WHERE
                    s.station = 'USC00519281'
            )
ORDER BY
    date