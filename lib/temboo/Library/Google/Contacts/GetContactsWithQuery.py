
###############################################################################
#
# GetContactsWithQuery
# Retrieves the contact or contacts in that account that match a specified query term.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetContactsWithQuery(Choreography):

    """
    Create a new instance of the GetContactsWithQuery Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Contacts/GetContactsWithQuery')


    def new_input_set(self):
        return GetContactsWithQueryInputSet()

    def _make_result_set(self, result, path):
        return GetContactsWithQueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetContactsWithQueryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetContactsWithQuery
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetContactsWithQueryInputSet(InputSet):
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
        Set the value of the Query input for this choreography. ((required, string) The contact criteria to search for, such as name or email address.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used whenever your access token expires.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the GetContactsWithQuery choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetContactsWithQueryResultSet(ResultSet):
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
        Retrieve the value for the "ContactID" output from this choreography execution. ((string) The unique ID string for the retrieved contact. If more than one contact is retrieved by the request, only the first contact's ID is output.)
        """
        def get_ContactID(self):
            return self._output.get('ContactID', None)
        """
        Retrieve the value for the "Link" output from this choreography execution. ((string) The unique edit link for the retrieved contact. If more than one contact is retrieved by the request, only the first contact's edit link is output.)
        """
        def get_Link(self):
            return self._output.get('Link', None)

class GetContactsWithQueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetContactsWithQueryResultSet(response, path)
