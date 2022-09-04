from django.test import TestCase
from helpdesk.models import Ticket,User
# Create your tests here.

class TicketTestCase(TestCase):
    def setUp(self):
        Ticket.objects.create(
            title = "Title", 
            subject = "Subject" ,
            priority = "Immediate",
            description = "Description",
            submittedby = User.objects.create(username="Name")
            )

    def test_ticket_edit(self):
        
        TEST1 = Ticket.objects.get(title = "Title")
        self.assertEqual(TEST1.title, "Title")
        self.assertEqual(TEST1.subject, "Subject")
        self.assertEqual(TEST1.priority, "Immediate")
        self.assertEqual(TEST1.description, "Description")
        self.assertEqual(TEST1.submittedby.username,"Name")
        
        self.assertEqual(TEST1._meta.get_field('title').max_length,  100)
        self.assertEqual(TEST1._meta.get_field('subject').max_length,  100)
        self.assertEqual(TEST1._meta.get_field('priority').max_length,  9)
        self.assertEqual(TEST1._meta.get_field('description').max_length, 10000)

    