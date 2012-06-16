
###############################################################################
#
# UpdateContact
# Update an existing contact's information.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateContact(Choreography):

    """
    Create a new instance of the UpdateContact Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Contacts/UpdateContact')


    def new_input_set(self):
        return UpdateContactInputSet()

    def _make_result_set(self, result, path):
        return UpdateContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateContactChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateContact
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateContactInputSet(InputSet):
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
        Set the value of the NewEmail input for this choreography. ((optional, string) The contact's new email address.)
        """
        def set_NewEmail(self, value):
            InputSet._set_input(self, 'NewEmail', value)

        """
        Set the value of the NewFirstName input for this choreography. ((optional, string) The contact's new first name.)
        """
        def set_NewFirstName(self, value):
            InputSet._set_input(self, 'NewFirstName', value)

        """
        Set the value of the NewLastName input for this choreography. ((optional, string) The contact's new last name.)
        """
        def set_NewLastName(self, value):
            InputSet._set_input(self, 'NewLastName', value)

        """
        Set the value of the NewPhone input for this choreography. ((optional, string) The contact's new telephone number.)
        """
        def set_NewPhone(self, value):
            InputSet._set_input(self, 'NewPhone', value)

        """
        Set the value of the Query input for this choreography. ((required, string) A search term to retrieve the contact to update, such as an email address, last name, or address. Be specific to not retrieve more than one contact.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateContact choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateContactResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)
        """
        Retrieve the value for the "ContactID" output from this choreography execution. ((string) The unique ID for the contact returned by Google.)
        """
        def get_ContactID(self):
            return self._output.get('ContactID', None)
        """
        Retrieve the value for the "Email" output from this choreography execution. ((string) The contact's current email address.)
        """
        def get_Email(self):
            return self._output.get('Email', None)
        """
        Retrieve the value for the "FirstName" output from this choreography execution. ((string) The contact's current given name.)
        """
        def get_FirstName(self):
            return self._output.get('FirstName', None)
        """
        Retrieve the value for the "LastName" output from this choreography execution. ((string) The contact's current family name.)
        """
        def get_LastName(self):
            return self._output.get('LastName', None)
        """
        Retrieve the value for the "Phone" output from this choreography execution. ((string) The contact's current telephone number.)
        """
        def get_Phone(self):
            return self._output.get('Phone', None)

class UpdateContactChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateContactResultSet(response, path)
