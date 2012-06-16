
###############################################################################
#
# AssociateAccount
# Creates an association between the developer and the publisher. If an association already exists, the method does nothing.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AssociateAccount(Choreography):

    """
    Create a new instance of the AssociateAccount Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AccountService/AssociateAccount')


    def new_input_set(self):
        return AssociateAccountInputSet()

    def _make_result_set(self, result, path):
        return AssociateAccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AssociateAccountChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AssociateAccount
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AssociateAccountInputSet(InputSet):
        """
        Set the value of the DeveloperURL input for this choreography. ((string) The site to be associated with this publisher.)
        """
        def set_DeveloperURL(self, value):
            InputSet._set_input(self, 'DeveloperURL', value)

        """
        Set the value of the Email input for this choreography. ((string) The developer's email address.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) One of either 'sandbox.google.com' (for testing) or 'www.google.com'. Defaults to 'sandbox.google.com'.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Password input for this choreography. ((string) The developer's password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Phone input for this choreography. ((integer) The last five digits of the publisher's phone number, in the form '99999'.)
        """
        def set_Phone(self, value):
            InputSet._set_input(self, 'Phone', value)

        """
        Set the value of the PostalCode input for this choreography. ((integer) The publisher's 5-digit postal code.)
        """
        def set_PostalCode(self, value):
            InputSet._set_input(self, 'PostalCode', value)

        """
        Set the value of the PublisherEmail input for this choreography. ((string) The publisher's email address.)
        """
        def set_PublisherEmail(self, value):
            InputSet._set_input(self, 'PublisherEmail', value)


"""
A ResultSet with methods tailored to the values returned by the AssociateAccount choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AssociateAccountResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google AdSense.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AssociateAccountChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AssociateAccountResultSet(response, path)
