from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Введите оригинальную ссылку',
        validators=[
            DataRequired('Обязательное поле'),
            Length(1, 256),
            URL('Требуется вставить ссылку')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки(необязательно)',
        validators=[
            Optional(),
            Length(1, 256),
            URL('Требуется вставить ссылку')
        ]
    )
    
    submit = SubmitField('Создать')