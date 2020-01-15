Schema
======



**Import Module**

.. code-block:: python

    from pytonik.Driver import Schema



**Callable**

.. code-block:: python

    DB = Schema.Schema()


**Drop**

.. code-block:: python

    DB.table('users').exists().drop()



.. code-block:: python

    DB.table('users').drop()


Selects
-------

**Specifying A Select Clause**

You may not always want to select allcolumns from a database table. Using the select method,
you can specify a custom select clause for the query:

.. code-block:: python

    DB.table('users').select().get()



.. code-block:: python

    DB.table('users').where('username', 'pytonik').select().get()

.. code-block:: python

    DB.table('users').where('users_id', '=', 1).select().get().result


The ``distinct`` method allows you to force the query to return distinct results:


.. code-block:: python

    DB.table('transactions').distinct('amount').select().get().result



The ``COUNT`` method allows you to force the query to return COUNT results:


.. code-block:: python

    DB.table('users').select().count()


The ``count`` method allows you to force the query to return row count results:

.. code-block:: python

    DB.table('users')..where('users_id', '=', 1).select().get().count


Raw Expressions
---------------

Sometimes you may need to use a raw expression in a query. To create a raw expression,
you may use the DB.raw:

.. code-block:: python

    DB.table('users').where('status', '<>', 1).groupBy('status').select(DB.raw('count(*) as user_count, status')).get()


Raw statements will be injected into the query as strings, so you should be extremely careful to not create SQL
injection vulnerabilities.


Raw Methods
-----------

Instead of using DB.raw, you may also use the following methods to insert a raw expression into various parts of
your query. ``selectRaw``



The ``selectRaw`` method can be used in place of select(DB.raw(...)). This method accepts an optional array of
bindings as its second argument:

.. code-block:: python

    orders = DB.table('orders').selectRaw('price * ? as price_with_tax').get();


The ``havingRaw`` and ``orHavingRaw`` methods may be used to set a raw string as the value of the having clause.
These methods accept an optional array of bindings as their second argument:

.. code-block:: python

    orders = DB.table('orders').groupBy('department').havingRaw('SUM(price) > ?', '').select('department', DB.raw('SUM(price) as total_sales')).get()

The whereRaw and orWhereRaw methods can be used to inject a raw where clause into your query.
These methods accept an optional array of bindings as their second argument:

.. code-block:: python

    orders = DB.table('orders').whereRaw('price > IF(state = "TX", ?, 100)', [200]).get();


.. code-block:: python

    DB.table('users').where('users_id', 1).delete()


.. code-block:: python

    DB.table('users').value('users_username', 'email').select().get()


.. code-block:: python

    DB.table('users').where('users_id', '=', 1).value('users_username','users_email').select().get()



.. code-block:: python

    DB.table('users').groupBy('users_id').select().get()


.. code-block:: python

    DB.table('users').orderBy('users_id', 'desc').select().get()


.. code-block:: python

    DB.table('users').groupBy('users_id').orderBy('users_id', 'desc').select().get()


.. code-block:: python

    DB.table('users').limit(1).select().get()


.. code-block:: python

    DB.table('users').offset(1).limit(2).select().get().result


.. code-block:: python

    DB.table('users').offset(1).limit(2).select().get().result

.. code-block:: python

    DB.table('users').join('message', 'users.users_id', '=', 'message.users_id').select().get()

.. code-block:: python

    DB.table('users').join('message', 'message.users_id', '=', 'users.users_id').leftJoin('bank', 'mlm_users_bank.users_username', '=', 'mlm_users.users_username').select().get()


.. code-block:: python

    DB.table('users').join('message', 'message.users_id', '=', 'users.users_id ').rightJoin('bank', 'bank.users_id', '=', 'users.users_id').select().get()



.. code-block:: python

    insert = DB.table('users').insert(
            [
            dict(email ='info@pytonik.com', name= 'Pytonik MVC', created_at='2020-02-05 09:02:08.26'),
            ])

.. code-block:: python

    insert = DB.table('users').insert(
            [
            dict(email ='info@pytonik.com', name= 'Pytonik MVC', created_at='2020-02-05 09:02:08.26'),
            dict(email ='dev@pytonik.com', name = 'Pytonik Moduel', created_at='2020-02-05 09:02:08.26'),
            ])


.. code-block:: python

    DB.table('users').where('id', '=', 18).update([dict(email='info@pytonik.com')]))

.. code-block:: python

    DB.table('transactions').max('amount').select().get().result)


.. code-block:: python

    DB.table('transactions').min('amount').select().get().result

.. code-block:: python

    DB.table('transactions').avg('amount').select().get().result



.. code-block:: python

    DB.table('transactions').counts().select().get().result



.. code-block:: python

    DB.table('transactions').pluck('transactions_referno', 'name').select().get().result



.. code-block:: python

    DB.table('transactions').find(3)

.. code-block:: python

    DB.table('transactions').where('him', '>', 1).whereNotIn('book_price', ['100','200', '300', '809']).select()



.. code-block:: python

    tableb.where('him', '1').where('him', '1').where('him', '1').select('examId')


.. code-block:: python

    tableb.where('him', '44').where('him', '2').where('him', '80').select()

.. code-block:: python

    tableb.where('you', '1w').where('you', '12').where('you', '87').orWhere('you', '22').select('examId')

.. code-block:: python

    tableb.where('blog_status', '=', 'stay').fromTable('menu').outerJoin(tableb.selectRaw("(SELECT menu_parent, COUNT(*) AS Count FROM mlm_menu GROUP BY menu_parent) as"), 'a.menu_id', 'sub.menu_parent ').select('a.menu_id', 'a.menu_name', 'a.menu_status', 'a.menu_link', 'sub.Count')

.. code-block:: python

    tableb.whereColumn('first_name', '>', 'last_name')

.. code-block:: python

    tableb.whereColumn(('first_name', '=', 'last_name'),('updated_at', '>', 'created_at'))

.. code-block:: python

    tableb.join('contacts', 'users.id', '=', 'contacts.user_id').join('orders', 'users.id', '=', 'orders.user_id').select('users.*', 'contacts.phone', 'orders.price')


.. code-block:: python

   DB.table('transactions').whereBetween('votes', ['30']).select()


.. code-block:: python

    DB.table('transactions').whereNotBetween('votes', ['1', '100', '30']).select()

.. code-block:: python

    DB.table('users').join('contacts', 'users.id', '=', 'contacts.user_id').join('orders', 'users.id', '=', 'orders.user_id').select('users.*', 'contacts.phone', 'orders.price')