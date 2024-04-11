# Entity Relationship Model

- The Chen notation favors conceptual modeling
- The Crow's foot notation favors a more implementation-oriented approach.
- The UML notation can be used for boh Conceptual and Implementation modeling


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/ceaaf140-2c04-4438-b01d-57cead3cc012)

- Derived Attributes: An attribute whose value is calculated from other attributes.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/ab94e36c-bc03-4fa4-9184-fd1a41132d98)



#### Connectivity and Cardinality

- The term connectivity is used to describe the relationship classification (ex: one to many)
- Cardinality express the minimum and maximum number of entity ocurrences associated with oe ocurrence of the related entity. 

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/4c463c49-0219-4848-b694-9c0caf7cdbdc)


#### Existence Dependece
An entity is said to be existence-dependent if it can exist in the database only when it is associated with another related entity occurrence.

If an entity can exists apart from all of its related entities, then it is said to be existence-independent.

#### Relationship Strength

- A week relationship, also known as a non-identifying relationship, exits if the primary key of the related entity does not contan a primary key component of the parent entity.
- A Strong relationship existis when the primary key of the related entity contains a primary key component of the parent entity.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/0059b460-2cd7-4f93-9b27-c00af1330360)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/00935651-aedc-442d-aa59-699d1cc26d3e)

#### Weak Entities

a weak entity is one that meets two conditions:

1. The entity is existence-dependent, it cannot exist without the entity with which it has a relationship.
2. The entity has a primary key that is partially or totally derived from the parent entity in the relationship


#### Relationship Degree

A relationship Degree indicates the number of entities or participants associated with a relationship. A unary relationship existis when an association is maintained within a single entity.
A binary relationship exists when two entities are associated. A ternary exists when three entities are associated.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/7dbff3c7-1e57-4897-980f-13f4ee5c7069)


#### Recursive Relationships

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/8053329c-ff30-41c9-8b8a-404e1f047f7f)

#### Associated (Composite) Entities

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/a7dd6609-7634-4ba5-975c-17301ffacd35)
![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/3ada4af7-be45-421c-9d5b-0236936e399f)




## Developing an ER Diagram

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/da6a7279-73c4-4004-80e6-2c5ade27cac8)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/21417bd1-2a57-4725-bf8a-a8f65a3e76c7)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/2a034de2-0eac-4609-ae70-6ba62259b4b7)
