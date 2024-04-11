# The relational Database Model

Relational database model enables logical represtation of the data and its relationships
- Logical simplicity produces simple and effective database design methodologies
- The logical view is facilitated by creating data relationships based on a logical construct called a relation.

- ### Chaacteristics of a Relational Table

- ![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/6565de34-7c45-4988-9cde-3258cd24983c)

- ## Keys

- A key consists of one or more attributes that determine other attributes

- ### Dependencies

- The role of a key is based on the concept of determination. Determination is the state in which 
knowing the value of one attribute makes it possible to determine the value of another

The relationship is called functional dependence, which means that the value of one or more attributes determines the 
value of one or more other attributes

In this functional dependency, the attribute whose value determines another is called the determinant or the key. The attribute whose value is determined by the other attribute is called the dependent

### Types of Keys

- Composite Key: a key composed of more than one attribute. (an attribute that is part of a key is a key attribute)
- Superkey: is a key that can uniquely identify any row in the table.
- Candidate key: is a minimal superkey, a superkey without any unnecessary attributes.
- Foreign Key (FK): primary key of one table that has been placed into another table to create a common attribute.
- Secondary Key: is adefined as a key that is used strictly for data retrieval purposes and does not require a functional dependency.

## Relational Algebra

Relational algebra defines the theoretical way of manipulating table contents 
using relational operators

### Relational Set Operators

SELECT (or RESTRICT), 
PROJECT, UNION, INTERSECT, DIFFERENCE, PRODUCT, JOIN, and DIVIDE 
operators.

- PROJECT yields all values for selected attributes.
- UNION combines all rows from two tables, excluding duplicate rows
- INTERSECT yields only the rows that appear in both tables
- DIFFERENCE yields all rows in one table that are not found in the other table
- PRODUCT yields all possible pairs of rows from two tables
- JOIN allows information to be intelligently combined from two or more tables

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/52cfa053-23c6-4a85-9e38-9c380098d538)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/2680c531-0d91-48a2-bb18-2857cf3efdf5)

### Types of join

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/84499d2b-57b8-4566-b302-6c97330ae055)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/2d2bfc8a-23c6-4601-8ee6-6cb602f97c1f)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/43017acc-e043-46ad-9f56-eb0d9fda604a)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/33b789d5-81a9-412e-836f-f14a02945660)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/3f51edbc-9980-44e4-97aa-4d762169240b)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/76030122-83e8-4642-9aa4-a225dd5fb535)

- Divide: The DIVIDE operator uses one double-column table as the dividend and one single-column table as the divisor
- ![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/8ef39577-7fec-43ca-b3ac-e33090dbbb4b)

## Data Dictionary 

The data dictionary provides a detailed description of all tables in the database created by the 
user and designer

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/21800bc2-bd77-415d-99fb-0250a80c787a)
(hd)



