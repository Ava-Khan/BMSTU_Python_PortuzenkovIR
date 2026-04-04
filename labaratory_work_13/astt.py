class Number:
    def __init__(self, value):
        self.value = value
    def eval(self, context):
        return int(self.value)

class Boolean:
    def __init__(self, value):
        self.value = value
    def eval(self, context):
        return self.value.lower() == 'true'

class Variable:
    def __init__(self, name):
        self.name = name
    def eval(self, context):
        return context.get(self.name)

class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Sum(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) + self.right.eval(context)

class Sub(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) - self.right.eval(context)

class Mul(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) * self.right.eval(context)

class Div(BinaryOp):
    def eval(self, context):
        right_val = self.right.eval(context)
        if right_val == 0:
            raise ValueError("Деление на ноль")
        return self.left.eval(context) / right_val

class Assign(BinaryOp):
    def eval(self, context):
        value = self.right.eval(context)
        context[self.left.name] = value
        return value

class Equals(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) == self.right.eval(context)

class LessThan(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) < self.right.eval(context)

class GreaterThan(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) > self.right.eval(context)

class Print:
    def __init__(self, value):
        self.value = value
    def eval(self, context):
        print(self.value.eval(context))

class WhileLoop:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def eval(self, context):
        result = None
        while self.condition.eval(context):
            result = self.body.eval(context)
        return result

class Block:
    def __init__(self, statements):
        self.statements = statements
    def eval(self, context):
        result = None
        for statement in self.statements:
            result = statement.eval(context)
        return result