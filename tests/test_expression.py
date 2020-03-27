from app import db
from app.models.models import User, Expression

expression_template1 = {
            'expression': "x + 2 = 5",
            'expression_type': "equation",
            'solutions': "3",
            'step': " ",
            'plot': " ",
            'alternate_forms': " ",
            'execution_time': "1"
}

expression_template2 = {
            'expression': "x + 3 = 5",
            'expression_type': "equation",
            'solutions': "2",
            'step': " ",
            'plot': " ",
            'alternate_forms': " ",
            'execution_time': "1"
}

def test_create_expression(app):
    ex = Expression(**expression_template1)
    user = User(username="user1", password="password1", token="token1")
    user.expressions.append(ex)
    db.session.add(user)
    db.session.commit()
    expressions = Expression.query.all()
    assert len(expressions) == 1
    assert expressions[0].expression == ex.expression
    assert expressions[0].solutions == ex.solutions
    assert expressions[0].expression_type == ex.expression_type
    assert expressions[0].execution_time == ex.execution_time
    assert expressions[0].user_id == user.id

def test_del_user_cascade(app):
    user = User(username="user1", password="password1", token="token1")
    ex1 = Expression(**expression_template1)
    user.expressions.append(ex1)
    ex2 = Expression(**expression_template2)
    user.expressions.append(ex2)
    db.session.add(user)
    db.session.commit()

    obj = User.query.filter_by(id=1).one()
    db.session.delete(obj)
    db.session.commit()

    expressions = Expression.query.all()
    assert len(expressions) == 0

    user1 = User(username="user1", password="password1", token="token1")
    ex1 = Expression(**expression_template1)
    user1.expressions.append(ex1)
    ex2 = Expression(**expression_template2)
    user1.expressions.append(ex2)
    user2 = User(username="user2", password="password2", token="token2")
    ex3 = Expression(**expression_template2)
    user2.expressions.append(ex3)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    obj = User.query.filter_by(id=1).one()
    db.session.delete(obj)
    db.session.commit()

    expressions = Expression.query.all()
    assert len(expressions) == 1

def test_del_expression(app):
    user1 = User(username="user1", password="password1", token="token1")
    user2 = User(username="user2", password="password2", token="token2")
    ex1 = Expression(**expression_template1)
    ex2 = Expression(**expression_template2)
    ex3 = Expression(**expression_template2)
    user1.expressions.append(ex1)
    user1.expressions.append(ex2)  
    user2.expressions.append(ex3)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()  

    ex_to_del = Expression.query.filter_by(user_id=1, expression = "x + 2 = 5").one()
    db.session.delete(ex_to_del)
    db.session.commit()

    expressions = Expression.query.all()
    assert len(expressions) == 2

    