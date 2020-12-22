-- Query 1
SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
FROM 
	employees e
	JOIN salaries s on e.emp_no = s.emp_no;

-- Query 2
SELECT 
	first_name,
	last_name,
	hire_date
FROM 
	employees e
WHERE 
	(hire_date >= '1986-01-01 00:00:00'::timestamp)
	AND  
	(hire_date <  '1986-12-31 23:59:59'::timestamp)
ORDER BY
	hire_date asc, last_name asc;
	
-- Query 3
SELECT
	dm.dept_no,
	d.dept_name,
	dm.emp_no,
	e.last_name,
	e.first_name
FROM 
	dept_managers dm
	JOIN employees e on dm.emp_no = e.emp_no
	JOIN departments d on dm.dept_no = d.dept_no;
	
-- Query 4
SELECT
	de.emp_no,
	e.last_name,
	e.first_name,
	d.dept_no
FROM 
	departments d
	JOIN dept_emp de on d.dept_no = de.dept_no
	JOIN employees e on de.emp_no = e.emp_no
ORDER BY
	last_name asc;
	
-- Query 5
SELECT
	first_name,
	last_name,
	sex
FROM 
	employees
WHERE
	first_name = 'Hercules' AND
	last_name LIKE 'B%'
ORDER BY
	last_name asc;
	
-- Query 6
SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM 
	departments d
	JOIN dept_emp de on d.dept_no = de.dept_no
	JOIN employees e on de.emp_no = e.emp_no
WHERE
	d.dept_name = 'Sales'
ORDER BY
	last_name asc;

-- Query 7
SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM 
	departments d
	JOIN dept_emp de on d.dept_no = de.dept_no
	JOIN employees e on de.emp_no = e.emp_no
WHERE
	d.dept_name = 'Sales' OR
	d.dept_name = 'Development'
ORDER BY
	dept_name asc, last_name asc;
	
-- Query 8
SELECT
	last_name,
	COUNT(*) AS frequency
FROM 
	employees
GROUP BY
	last_name
ORDER BY
	frequency desc

 
