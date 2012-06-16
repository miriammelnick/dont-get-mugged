
###############################################################################
#
# GetStandardFeeds
# Retrieve a list of videos that reflect YouTube user behavior, or that were selected by YouTube staff.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetStandardFeeds(Choreography):

    """
    Create a new instance of the GetStandardFeeds Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/YouTube/GetStandardFeeds')


    def new_input_set(self):
        return GetStandardFeedsInputSet()

    def _make_result_set(self, result, path):
        return GetStandardFeedsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetStandardFeedsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetStandardFeeds
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetStandardFeedsInputSet(InputSet):
        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) Specify the maximum number of results to return. The default value is 10, the maximum value is 50.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the StartIndex input for this choreography. ((optional, integer) Specify the first matching result to return. Uses a one-based index (the first result is 1 by default).)
        """
        def set_StartIndex(self, value):
            InputSet._set_input(self, 'StartIndex', value)

        """
        Set the value of the Time input for this choreography. ((optional, string) Restrict the response to results relevant to the specified time frame. Valid values: today, this_week, this_month, and all_time (the default))
        """
        def set_Time(self, value):
            InputSet._set_input(self, 'Time', value)

        """
        Set the value of the Type input for this choreography. ((string) Enter top_rated, top_favorites, most_viewed, most_shared, most_popular, most_recent, most_discussed, most_responded, recently_featured, or on_the_web.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the GetStandardFeeds choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetStandardFeedsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The result set returned by the API call.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetStandardFeedsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetStandardFeedsResultSet(response, path)
