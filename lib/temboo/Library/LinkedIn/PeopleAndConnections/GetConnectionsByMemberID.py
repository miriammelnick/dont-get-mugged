
###############################################################################
#
# GetConnectionsByMemberID
# Retrieve all connections linked to a  member ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetConnectionsByMemberID(Choreography):

    """
    Create a new instance of the GetConnectionsByMemberID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/PeopleAndConnections/GetConnectionsByMemberID')


    def new_input_set(self):
        return GetConnectionsByMemberIDInputSet()

    def _make_result_set(self, result, path):
        return GetConnectionsByMemberIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetConnectionsByMemberIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetConnectionsByMemberID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetConnectionsByMemberIDInputSet(InputSet):
        """
        Set the value of the MemberID input for this choreography. ((required, integer) Enter a LinkedIn Member ID.)
        """
        def set_MemberID(self, value):
            InputSet._set_input(self, 'MemberID', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by LinkedIn after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by LinkedIn after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The Oauth Token Secret retrieved during the Oauth process.)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Oauth Token retrieved during the Oauth process.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)


"""
A ResultSet with methods tailored to the values returned by the GetConnectionsByMemberID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetConnectionsByMemberIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from LinkedIn in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetConnectionsByMemberIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetConnectionsByMemberIDResultSet(response, path)
