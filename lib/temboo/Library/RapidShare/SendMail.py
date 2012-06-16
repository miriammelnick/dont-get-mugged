
###############################################################################
#
# SendMail
# Send an email that contains a link to a file available on RapidShare.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SendMail(Choreography):

    """
    Create a new instance of the SendMail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/SendMail')


    def new_input_set(self):
        return SendMailInputSet()

    def _make_result_set(self, result, path):
        return SendMailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendMailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SendMail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SendMailInputSet(InputSet):
        """
        Set the value of the Comment input for this choreography. ((string) A comment that you want to send with the email)
        """
        def set_Comment(self, value):
            InputSet._set_input(self, 'Comment', value)

        """
        Set the value of the Email1 input for this choreography. ((string) The first email address to send to)
        """
        def set_Email1(self, value):
            InputSet._set_input(self, 'Email1', value)

        """
        Set the value of the Email2 input for this choreography. ((optional, string) The second email address to send to)
        """
        def set_Email2(self, value):
            InputSet._set_input(self, 'Email2', value)

        """
        Set the value of the Email3 input for this choreography. ((optional, string) The third email address to send to)
        """
        def set_Email3(self, value):
            InputSet._set_input(self, 'Email3', value)

        """
        Set the value of the FileID1 input for this choreography. ((integer) The id for the file to inform the email recipient about)
        """
        def set_FileID1(self, value):
            InputSet._set_input(self, 'FileID1', value)

        """
        Set the value of the FileName1 input for this choreography. ((string) The name of the file to inform the email recipient about)
        """
        def set_FileName1(self, value):
            InputSet._set_input(self, 'FileName1', value)

        """
        Set the value of the Login input for this choreography. ((string) Your RapidShare username)
        """
        def set_Login(self, value):
            InputSet._set_input(self, 'Login', value)

        """
        Set the value of the Name input for this choreography. ((string) The senders name)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the Password input for this choreography. ((string) Your RapidShare password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ReplyEmail input for this choreography. ((string) The sender reply email address)
        """
        def set_ReplyEmail(self, value):
            InputSet._set_input(self, 'ReplyEmail', value)

        """
        Set the value of the Subject input for this choreography. ((string) The subject line for the email)
        """
        def set_Subject(self, value):
            InputSet._set_input(self, 'Subject', value)


"""
A ResultSet with methods tailored to the values returned by the SendMail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SendMailResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from RapidShare)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SendMailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SendMailResultSet(response, path)
