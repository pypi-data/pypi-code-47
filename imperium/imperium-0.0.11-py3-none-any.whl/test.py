from evaluator import Expression

subject = {
    'maker': {
        'original': 'AUDI'
    },
    'model': {
        'original': 'A4'
    },
    'gearbox': {
        'original': 'Manuelle'
    },
    'energy': {
        'original': 'Diesel'
    }
}

expr = "exists('$subject.maker.original', $subject) and $subject['maker']['original'] == 'AUDI' and matches('(diesel)', $subject['energy']['original'], 'i')"

expression = Expression()
res = expression.evaluate(expr, subject)
print(res)