from flask import render_template, request, redirect, url_for, flash
from .models import Ticket
from . import db

from flask import current_app as app

@app.route('/')
def index():
    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)

@app.route('/ticket/<int:ticket_id>')
def ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    return render_template('ticket.html', ticket=ticket)

@app.route('/add', methods=['GET', 'POST'])
def add_ticket():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_ticket = Ticket(title=title, description=description)
        db.session.add(new_ticket)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_ticket.html')

@app.route('/edit/<int:ticket_id>', methods=['GET', 'POST'])
def edit_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    if request.method == 'POST':
        ticket.title = request.form['title']
        ticket.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_ticket.html', ticket=ticket)

@app.route('/delete/<int:ticket_id>')
def delete_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    flash('Ticket deleted successfully.')
    return redirect(url_for('index'))



