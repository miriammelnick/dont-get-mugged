
###############################################################################
#
# CreateContact
# Create a new contact.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateContact(Choreography):

    """
    Create a new instance of the CreateContact Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Contacts/CreateContact')


    def new_input_set(self):
        return CreateContactInputSet()

    def _make_result_set(self, result, path):
        return CreateContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateContactChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateContact
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateContactInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientID input for this choreography. ((required, string) The OAuth client ID provided by Google when you register your application.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((required, string) The OAuth client secret provided by Google when you registered your application.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The new contact's email address.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the FirstName input for this choreography. ((required, string) The new contact's first name.)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the LastName input for this choreography. ((required, string) The new contact's last name.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the Phone input for this choreography. ((required, string) The phone number for the new contact. It's best to use the "(555) 123-4567" format.)
        """
        def set_Phone(self, value):
            InputSet._set_input(self, 'Phone', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the CreateContact choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateContactResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)
        """
        Retrieve the value for the "ContactID" output from this choreography execution. ((string) The unique ID supplied by Google for the new user.)
        """
        def get_ContactID(self):
            return self._output.get('ContactID', None)

class CreateContactChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateContactResultSet(response, path)
