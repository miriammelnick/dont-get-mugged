
###############################################################################
#
# GetClicksForLink
# Returns the number of clicks on a single bitly link.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetClicksForLink(Choreography):

    """
    Create a new instance of the GetClicksForLink Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Bitly/LinkMetrics/GetClicksForLink')


    def new_input_set(self):
        return GetClicksForLinkInputSet()

    def _make_result_set(self, result, path):
        return GetClicksForLinkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetClicksForLinkChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetClicksForLink
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetClicksForLinkInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The oAuth access token provided by Bitly.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The result limit. Defaults to 100. Range is 1 to 1000.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Link input for this choreography. ((required, string) A bitly link.)
        """
        def set_Link(self, value):
            InputSet._set_input(self, 'Link', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Rollup input for this choreography. ((optional, boolean) Accepted values are true or false. When set to true, this returns data for multiple units rolled up to a single result instead of a separate value for each period of time.)
        """
        def set_Rollup(self, value):
            InputSet._set_input(self, 'Rollup', value)

        """
        Set the value of the Timestamp input for this choreography. ((optional, date) An epoch timestamp, indicating the most recent time for which to pull metrics.)
        """
        def set_Timestamp(self, value):
            InputSet._set_input(self, 'Timestamp', value)

        """
        Set the value of the Timezone input for this choreography. ((optional, string) An integer hour offset from UTC (-12..12), or a timezone string. Defaults to "America/New_York".)
        """
        def set_Timezone(self, value):
            InputSet._set_input(self, 'Timezone', value)

        """
        Set the value of the UnitName input for this choreography. ((optional, string) The unit of time that corresponds to query you want to run. Accepted values are: minute, hour, day, week, month, and day. Defaults to "day".)
        """
        def set_UnitName(self, value):
            InputSet._set_input(self, 'UnitName', value)

        """
        Set the value of the UnitValue input for this choreography. ((optional, integer) An integer representing the amount of time to query for. Corresponds to the UnitName input. Defaults to -1 indicating to return all units of time.)
        """
        def set_UnitValue(self, value):
            InputSet._set_input(self, 'UnitValue', value)


"""
A ResultSet with methods tailored to the values returned by the GetClicksForLink choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetClicksForLinkResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Bitly.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetClicksForLinkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetClicksForLinkResultSet(response, path)
