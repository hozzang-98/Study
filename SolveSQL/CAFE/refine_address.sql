SELECT
  substr(address, 1, instr(address, ' ') - 1) AS sido,
  substr(
    address,
    instr(address, ' ') + 1,
    instr(substr(address, instr(address, ' ') + 1), ' ') - 1
  ) AS sigungu,
  COUNT(*) as cnt
FROM
  cafes
GROUP BY sido, sigungu
ORDER BY cnt desc