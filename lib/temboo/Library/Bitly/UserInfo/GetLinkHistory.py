
###############################################################################
#
# GetLinkHistory
# Returns entries from a user's link history in reverse chronological order.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLinkHistory(Choreography):

    """
    Create a new instance of the GetLinkHistory Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Bitly/UserInfo/GetLinkHistory')


    def new_input_set(self):
        return GetLinkHistoryInputSet()

    def _make_result_set(self, result, path):
        return GetLinkHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLinkHistoryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLinkHistory
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLinkHistoryInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The oAuth access token provided by Bitly.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Archived input for this choreography. ((optional, string) Accepted values are: on|off|both.  Whether to include or exclude archived history entries. (on = return only archived history entries). Defaults to "off".)
        """
        def set_Archived(self, value):
            InputSet._set_input(self, 'Archived', value)

        """
        Set the value of the CreatedAfter input for this choreography. ((optional, date) An epoch timestamp representing a date to filter with.)
        """
        def set_CreatedAfter(self, value):
            InputSet._set_input(self, 'CreatedAfter', value)

        """
        Set the value of the CreatedBefore input for this choreography. ((optional, date) An epoch timestamp representing a date to filter with.)
        """
        def set_CreatedBefore(self, value):
            InputSet._set_input(self, 'CreatedBefore', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) An integer in the range of 1 to 100, specifying the max number of results to return. Defaults to 50.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Link input for this choreography. ((optional, string) The bitly link to return metadata for (when spcified, overrides all other options).)
        """
        def set_Link(self, value):
            InputSet._set_input(self, 'Link', value)

        """
        Set the value of the ModifiedAfter input for this choreography. ((optional, date) An epoch timestamp representing a date to filter with.)
        """
        def set_ModifiedAfter(self, value):
            InputSet._set_input(self, 'ModifiedAfter', value)

        """
        Set the value of the Offset input for this choreography. ((optional, string) An integer specifying the numbered result at which to start (used for pagination).)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the Private input for this choreography. ((optional, string) Accepted values are: on|off|both.  Whether to include or exclude archived history entries. (on = return only archived history entries). Defaults to "both".)
        """
        def set_Private(self, value):
            InputSet._set_input(self, 'Private', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the User input for this choreography. ((optional, string) The user for whom to retrieve history entries (if different from authenticated user).)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetLinkHistory choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLinkHistoryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Bitly.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLinkHistoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLinkHistoryResultSet(response, path)
