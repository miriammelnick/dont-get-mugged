
###############################################################################
#
# CheckinsByUser
# Retrieve a list of checkins for an authenticated user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CheckinsByUser(Choreography):

    """
    Create a new instance of the CheckinsByUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/CheckinsByUser')


    def new_input_set(self):
        return CheckinsByUserInputSet()

    def _make_result_set(self, result, path):
        return CheckinsByUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CheckinsByUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CheckinsByUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CheckinsByUserInputSet(InputSet):
        """
        Set the value of the AfterTimeStamp input for this choreography. ((optional, date) Retrieve the first results after the seconds entered since epoch time.)
        """
        def set_AfterTimeStamp(self, value):
            InputSet._set_input(self, 'AfterTimeStamp', value)

        """
        Set the value of the BeforeTimeStamp input for this choreography. ((optional, date) Retrieve the first results prior to the seconds specified. Useful for paging backward in time.)
        """
        def set_BeforeTimeStamp(self, value):
            InputSet._set_input(self, 'BeforeTimeStamp', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The total number of results to be returned, up to 250.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) The number of results to skip. Used to page through results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the UserID input for this choreography. ((optional, string) Only 'self' is supported at this moment by the Foursquare API. Defaults to: self.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the CheckinsByUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CheckinsByUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CheckinsByUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CheckinsByUserResultSet(response, path)
