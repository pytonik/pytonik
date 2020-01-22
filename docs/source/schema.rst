Schema
======

**pytonik** database query schema module provides a convenient, fluent interface to creating and running database queries.
It can be used to perform most database operations in your application and works on all supported database systems.



**Import Module**

.. code-block:: python

	from pytonik.Driver import Schema



**Callable**

.. code-block:: python

	DB = Schema.Schema()




**Tables**

.. code-block:: python



    TABLES = {}

    TABLES['users'] = (
            "CREATE TABLE `users` ("
            "  `users_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `birth_date` date NOT NULL,"
            "  `first_name` varchar(14) NOT NULL,"
            "  `last_name` varchar(16) NOT NULL,"
            "  `email` varchar(255) NOT NULL,"
            "  `votes` int(11) NOT NULL,"
            "  `create_date` date NOT NULL,"
            "  PRIMARY KEY (`emp_no`)"
            ") ENGINE=InnoDB")

    TABLES['banks'] = (
            "CREATE TABLE `banks` ("
            "  `banks_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `users_id` int(11) NOT NULL,"
            "  `bank_name` varchar(40) NOT NULL,"
            "  `bank_sort` varchar(40) NOT NULL,"
            "  PRIMARY KEY (`banks_id`)"
            ") ENGINE=InnoDB")

    TABLES['transactions'] = (
            "CREATE TABLE `transactions` ("
            "  `transaction_id` int(11) NOT NULL,"
            "  `users_id` int(11) NOT NULL,"
            "  `amount` varchar(40) NOT NULL,"
            "  `from_date` date NOT NULL,"
            "  `to_date` date NOT NULL,"
            "  PRIMARY KEY (`transaction_id`,`from_date`), KEY `transaction_id` (`transaction_id`),"
            ") ENGINE=InnoDB")

create
------

Create table using ``create`` method

.. code-block:: python

    DB.table(TABLES).create()


drop
----

If you wish to ``drop`` the entire table, you may use the ``drop`` method:


**Drop All**

.. code-block:: python

	DB.table('users').drop()


**Drop if Exist**

.. code-block:: python

	DB.table('users').exists().drop()





insert
------


The query schema also provides an insert method for inserting records into the database table.
The ``insert`` method accepts an array of column names and values:

.. code-block:: python

	insert = DB.table('users').insert(
			[
			dict(email ='info@pytonik.com', name= 'Pytonik MVC', created_at='2020-02-05 09:02:08.26'),
			])



**Multiple Insert**

You may even insert several records into the table with a single call to insert by passing an array of arrays.
Each ``dictionary`` inside ``list`` represents a row to be inserted into the table:


.. code-block:: python

	insert = DB.table('users').insertGetId(
			[
			dict(email ='dev@pytonik.com', name = 'Pytonik Moduel', created_at='2020-02-05 09:02:08.26'),
			])



**Auto-Incrementing IDs**

If the table has an auto-incrementing id, use the insertGetId method to insert a record and then retrieve the ID:


.. code-block:: python

	insert = DB.table('users').insert(
			[
			dict(email ='info@pytonik.com', name= 'Pytonik MVC', created_at='2020-02-05 09:02:08.26'),
			dict(email ='dev@pytonik.com', name = 'Pytonik Moduel', created_at='2020-02-05 09:02:08.26'),
			])

.. note::

    When using PostgreSQL the insertGetId method expects the auto-incrementing column to be named id. If you would like to retrieve the ID from a different ``sequence``,
    you may pass the column name as the second parameter to the insertGetId method.

update
------

In addition to inserting records into the database, the query schema can also update existing records using
the ``update`` method. The ``update`` method, like the ``insert`` method, accepts an ``dict`` of column and value pairs containing
the columns to be updated. You may constrain the update query using where clauses:

**Update**

.. code-block:: python

	DB.table('users').where('id', '=', 18).update([dict(email='info@pytonik.com')]))


delete
------

The query schema may also be used to ``delete`` records from the table via the delete method.
You may constrain delete statements by adding where clauses before calling the delete method:

.. code-block:: python

	DB.table('users').delete()


.. code-block:: python

	DB.table('users').where('users_id', 1).delete()





selects
-------


If you don't even need an entire row, you may extract a single value from a record using the value method. This method will return the value of the column directly:


.. code-block:: python

    DB.table('users').value('users_username', 'email').select().get()




.. code-block:: python

    DB.table('users').where('users_id', 18).select().get()


The query schema also provides a variety of aggregate methods such as ``counts``, ``max``, ``min``, ``avg``,
and ``sum``. You may call any of these methods after constructing your query:

**MAX()**

.. code-block:: python

	DB.table('transactions').max('amount').select().get()


**MIN()**


.. code-block:: python

	DB.table('transactions').min('amount').select().get()

**AVG**

.. code-block:: python

	DB.table('transactions').avg('amount').select().get()


**COUNT()**

.. code-block:: python

	DB.table('transactions').counts().select().get().result


You may combine these methods with other methods:

.. code-block:: python

	DB.table('transactions').where('status', 1).min('amount').select().get()



**Determining If Records Exist**

Instead of using the count method to determine if any records exist that match your query's constraints,
you may use the exists and ``notExist`` methods:

Example: **Exist**

.. code-block:: python

    DB.table('orders').where('finalized', 1).exists()

Example: **notExist**

.. code-block:: python

    DB.table('orders')->where('finalized', 1).notExist()


**Retrieving A Single Row / Column From A Table**

If you just need to retrieve a single row from the database table, you may use the first method.
This method will return a single dictionary object ``{}``:

.. code-block:: python

    user = DB::table('users')->where('status', 1)->first()

    print(user["name"])


**Retrieving A List Of Column Values**

If you would like to retrieve a Collection containing the values of a single column, you may use the pluck method.
In this example, we'll retrieve a Collection of role titles:

.. code-block:: python

    titles = DB::table('roles').pluck('title');

    for  title in titles:
         print(title)


You may also specify a custom key column for the returned Collection:

.. code-block:: python

    roles = DB.table('roles').pluck('title', 'name');

    for title in roles:

        print(title["name"])



If you need to work with thousands of database records, consider using the ``chunk`` method.
This method retrieves a small chunk of the results at a time and feeds each chunk into a Closure for processing.
This method is very useful for writing Artisan commands that process thousands of records.
For example, let's work with the entire users table in chunks of 100 records at a time:

.. code-block:: python

    DB.table('users').orderBy('id').chunk(100)



If you are updating database records while chunking results, your chunk results could change in unexpected ways. So,
when updating records while chunking, it is always best to use the chunkById method instead.
This method will automatically paginate the results based on the record's primary key:

.. code-block:: python

    users = DB.table('users').where('status ', 'PENDING').orderBy('users_id').chunk(100,
    DB.table('countries').where('users_id', '{users_id}').updates([dict(vote='200', create_at='20/01/2020')])
        )

.. note::

    When updating or deleting records inside the chunk callback, any changes to the primary key or foreign keys could affect the chunk query.
    This could potentially result in records not being included in the chunked results.


**Select Value**

If you don't even need an entire row, you may extract a single value from a record using the ``value`` method.
This method will return the value of the column directly

Example 1.0:

.. code-block:: python

    DB.table('users').select('users_username', 'email').get()


Example 1.1:

.. code-block:: python

    DB.table('users').value('users_username', 'email').select().get()



**Select Where with custom column**

Example 1.0:

.. code-block:: python

	DB.table('users').where('users_id', '=', 1).select('users_username','users_email').get()



Example 1.1:

.. code-block:: python

	DB.table('users').where('users_id', '=', 1).value('users_username','users_email').select().get()


**Select groupBy**

.. code-block:: python

    DB.table('users').groupBy('users_id').select().get()


**Select groupBy/having**

The ``groupBy`` and ``having`` methods may be used to group the query results.
The having method's signature is similar to that of the where method:

.. code-block:: python

    DB.table('users').groupBy('users_id').having('permission', '>', '100').select().get()


You may pass multiple arguments to the ``groupBy`` method to group by multiple columns:

.. code-block:: python

    DB.table('users')->groupBy('first_name', 'status')->having('permission', '>', '100').select().get()



**orderBy**



The ``orderBy`` method allows you to sort the result of the query by a given column.
The first argument to the ``orderBy`` method should be the column you wish to sort by,
while the second argument controls the direction of the sort and may be either ``asc`` or ``desc``:


.. code-block:: python

    DB.table('users').orderBy('users_id', 'desc').select().get()


.. code-block:: python

	DB.table('users').groupBy('users_id').orderBy('users_id', 'desc').select().get()


**limit**


To limit the number of results returned from the query, or to ``skip`` a given number of results in the query,
you may use the ``skip`` and ``take`` methods:

Example 1.0:

.. code-block:: python

   DB.table('users').skip(1).take(2).select().get()


**limit with offset**

Example 1.1:

.. code-block:: python

	DB.table('users').offset(1).limit(2).select().get()



Alternatively, you may use the limit and offset methods:


.. code-block:: python

   DB.table('users').limit(1).select().get()


**Select limit with offset**

Example 1.1:

.. code-block:: python

	DB.table('users').offset(1).limit(2).select().get()





where
-----

**Where having**

.. code-block:: python

    DB.table('users').where('status', 1).having('permission', '>', 2).select().get()

You may use the ``where`` method on a query schema instance to add ``where`` clauses to the query.

The most basic call to ``where`` requires three arguments. The first argument is the name of the column.
The second argument is an operator, which can be any of the database's supported operators.
Finally, the third argument is the value to evaluate against the column.



For example, here is a query that verifies the value of the "votes" column is equal to 100:


.. code-block:: python

    DB.table('users').where('votes', '=', 1).select().get()


For convenience, if you want to verify that a column is equal to a given value,
you may pass the value directly as the second argument to the where method:

.. code-block:: python

    DB.table('users').where('votes', 1).select().get()



You may use a variety of other operators when writing a ``where`` clause:


.. code-block:: python

    DB.table('users').where('votes', '>=', 100).select().get()

    DB.table('users').where('votes', '<>', 100).select().get()

    DB.table('users').where('votes', 'like', 'T%').select().get()




**Or Statements**

You may chain where constraints together as well as add or clauses to the query.
The ``orWhere`` method accepts the same arguments as the where method:


.. code-block:: python

    DB.table('users').where('user_id', 15).orWhere('user_id', 15).select('email')

**AND**

.. code-block:: python

	DB.table('users').where('user_id', 18).where('email', 'info@pytonik.com').select().get()

**OR**

.. code-block:: python

	DB.table('users').where('user_id', 18).orWhere('user_id', 15).select().get()

**AND/OR**

.. code-block:: python

	DB.table('users').where('user_id', 18).where('email', 'info@pytonik.com').orWhere('user_id', 15).select().get()




**Where Column**

The ``whereColumn`` method may be used to verify that two columns are equal:

.. code-block:: python

	DB.table('users').whereColumn('first_name', '>', 'last_name')


**Multiple Where Column**

.. code-block:: python

    DB.table('users').whereColumn(('first_name', '=', 'last_name'),('updated_at', '>', 'created_at'))


**Additional Where Clauses**

**Where Between**

The ``whereBetween`` method verifies that a column's value is between two values:

.. code-block:: python

   DB.table('transactions').whereBetween('votes', ['30']).select()

**Where Between**

The ``whereNotBetween`` method verifies that a column's value lies outside of two values:

.. code-block:: python

	DB.table('transactions').whereNotBetween('votes', ['1', '100', '30']).select()



**whereIn / whereNotIn**

The ``whereIn`` method verifies that a given column's value is contained within the given list:

.. code-block:: python

    DB.table('users').whereIn('id', [1, 2, 3]).select().get()

The ``whereNotIn`` method verifies that the given column's value is **not** contained in the given list:

.. code-block:: python

    DB.table('users').whereNotIn('id', [1, 2, 3]).select().get()



**whereNull / whereNotNull**


The ``whereNull`` method verifies that the value of the given column is ``NULL``:

.. code-block:: python

    DB.table('users').whereNull('updated_at').select().get()

The ``whereNotNull`` method verifies that the column's value is not ``NULL``:

.. code-block:: python

    DB.table('users').whereNotNull('updated_at').select().get()


The query schema also provides a quick way to ``union`` two queries together.
For example, you may create an initial query and use the ``union`` method to ``union`` it with a second query:

.. code-block:: python

    first = DB.table('username').select().set()

    users = DB.table('countries').orderBy('country_id').select().union(first).get()


.. note::

 The ``unionAll`` method is also available and has the same method signature as ``union``.


join
----

The query schema may also be used to write join statements.
To perform a basic ``inner join``, you may use the ``join`` method on a query schema instance.
The first argument passed to the join method is the name of the table you need to ``join`` to,
while the remaining arguments specify the column constraints for the join.
You can even join to multiple tables in a single query:

**Join**

.. code-block:: python

    DB.table('users').join('contacts', 'users.id', '=', 'contacts.user_id').select().get()




**Inner Join**

.. code-block:: python

    DB.table('users').join('contacts', 'users.id', '=', 'contacts.user_id').join('orders', 'users.id', '=', 'orders.user_id').select('users.*', 'contacts.phone', 'orders.price').get()




Left Join / Right Join
----------------------

If you would like to perform a "left join" or "right join" instead of an "inner join",
use the ``leftJoin`` or ``rightJoin`` methods. These methods have the same signature as the ``join`` method:

**left Join**

.. code-block:: python

	DB.table('users').leftJoin('bank', 'bank.users_id, '=', 'users.users_id').select().get()



**left Join with Join**

.. code-block:: python

	DB.table('users').leftJoin('bank', 'bank.users_id, '=', 'users.users_id').join('message', 'message.users_id', '=', 'users.users_id').select().get()




**right Join**

.. code-block:: python

    DB.table('users').rightJoin('bank', 'bank.users_id', '=', 'users.users_id').select().get()


**right Join with**

.. code-block:: python

    DB.table('users').rightJoin('bank', 'bank.users_id', '=', 'users.users_id').join('message', 'message.users_id', '=', 'users.users_id').select().get()

**left outer Join**

.. code-block:: python

    DB.table('comment').where('comment_status', '=', 1).fromTable('comment').outerJoin(DB.raw("(SELECT parent_id, COUNT(*) AS comment FROM parent GROUP BY parent_id) as sub"), 'comment_id', 'sub.parent_id ').select('a.comment_id', 'a.comment_name', 'a.comment_status', 'a.comment_link', 'sub.Count')


**Advanced Join**

You may also specify more advanced join. To get started, pass a Closure as the second argument into
the ``join`` method. The Closure will receive a JoinClause object which allows you to specify constraints on the
join clause:


.. code-block:: python

    DB.table('users').join('bank', 'bank.users_id', '=', 'users.users_id').where('bank.status', '>', 5).select().get()


If you would like to use a "where" style clause on your joins, you may use the ``where`` and ``orWhere`` methods
on a join.
Instead of comparing two columns, these methods will compare the column against a value:



Raw Expressions
---------------

Sometimes you may need to use a raw expression in a query. To create a raw expression, you may use the ``DB.raw`` method:

**DB.raw**

.. code-block:: python

    DB.table('users').where('status', '>', 1).groupBy('status').select(DB.raw('count(*) as user_count, status')).get()
    

