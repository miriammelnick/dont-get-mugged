
###############################################################################
#
# DeleteContact
# Deletes a specified contact.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteContact(Choreography):

    """
    Create a new instance of the DeleteContact Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Contacts/DeleteContact')


    def new_input_set(self):
        return DeleteContactInputSet()

    def _make_result_set(self, result, path):
        return DeleteContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteContactChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteContact
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteContactInputSet(InputSet):
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
        Set the value of the ContactID input for this choreography. ((required, string) The unique ID string for the contact you want to delete.)
        """
        def set_ContactID(self, value):
            InputSet._set_input(self, 'ContactID', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteContact choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteContactResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Google. No content is returned for a successful delete request.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((required, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)

class DeleteContactChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteContactResultSet(response, path)
