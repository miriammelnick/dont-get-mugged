
###############################################################################
#
# FindUsers
# Allows a user to locate friends.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FindUsers(Choreography):

    """
    Create a new instance of the FindUsers Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/FindUsers')


    def new_input_set(self):
        return FindUsersInputSet()

    def _make_result_set(self, result, path):
        return FindUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindUsersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FindUsers
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FindUsersInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((conditional, string) A comma-delimited list of email addresses to look for. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the FacebookID input for this choreography. ((conditional, string) A comma-delimited list of Facebook ID's to look for. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        def set_FacebookID(self, value):
            InputSet._set_input(self, 'FacebookID', value)

        """
        Set the value of the Name input for this choreography. ((conditional, string) A single string to search for in users' names. A single string to search for in users' names. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Phone input for this choreography. ((conditional, string) A comma-delimited list of phone numbers to look for. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        def set_Phone(self, value):
            InputSet._set_input(self, 'Phone', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the TwitterSource input for this choreography. ((conditional, string) A single Twitter handle. Results will be users that this handle follows on Twitter who use Foursquare. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        def set_TwitterSource(self, value):
            InputSet._set_input(self, 'TwitterSource', value)

        """
        Set the value of the Twitter input for this choreography. ((conditional, string) A comma-delimited list of Twitter handles to look for. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        def set_Twitter(self, value):
            InputSet._set_input(self, 'Twitter', value)


"""
A ResultSet with methods tailored to the values returned by the FindUsers choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FindUsersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FindUsersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindUsersResultSet(response, path)
