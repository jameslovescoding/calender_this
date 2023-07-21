from flask_wtf import FlaskForm

from wtforms.fields import (
    BooleanField,
    DateField,
    StringField,
    SubmitField,
    TextAreaField,
    TimeField
)

from wtforms.validators import (DataRequired, ValidationError)

from datetime import datetime

class AppointmentForm(FlaskForm):
  name = StringField("Name", validators=[DataRequired()])
  start_date = DateField("Start Date", validators=[DataRequired()])
  start_time = TimeField("Start Time", validators=[DataRequired()])
  end_date = DateField("End Date", validators=[DataRequired()])
  end_time = TimeField("End Time", validators=[DataRequired()])
  description = TextAreaField("Description", validators=[DataRequired()])
  private = BooleanField("Private?")
  submit = SubmitField('Create new appointment')

  def validate_end_date(form, field):
    start = datetime.combine(form.start_date.data, form.start_time.data)
    end = datetime.combine(field.data, form.end_time.data)
    if start >= end:
      msg = "End date/time must come after start date/time"
      raise ValidationError(msg)
    start_date = form.start_date.data
    end_date = form.end_date.data
    if start_date != end_date:
      msg = "Start date and end date should be the same day"
      raise ValidationError(msg)