
###############################################################################
#
# GetMetrics
# Retrieves metrics such as visits, page views, bounces within a specified time frame.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetMetrics(Choreography):

    """
    Create a new instance of the GetMetrics Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Analytics/GetMetrics')


    def new_input_set(self):
        return GetMetricsInputSet()

    def _make_result_set(self, result, path):
        return GetMetricsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMetricsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetMetrics
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetMetricsInputSet(InputSet):
        """
        Set the value of the Dimensions input for this choreography. ((optional, string) Defines the primary data keys for your Analytics report. Use dimensions to segment your web property metrics (e.g.  ga:browser or ga:city).)
        """
        def set_Dimensions(self, value):
            InputSet._set_input(self, 'Dimensions', value)

        """
        Set the value of the EndDate input for this choreography. ((required, date) The end date for the range of data you want to retrieve. Epoch timestamp in milliseconds or formatted as yyyy-MM-dd.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the Filters input for this choreography. ((optional, string) Restricts the data returned by a dimension or metric you want to filter by using an expression (i.e. ga:timeOnPage==10).)
        """
        def set_Filters(self, value):
            InputSet._set_input(self, 'Filters', value)

        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) The max results to be returned in the feed. Defaults to 50.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the Metrics input for this choreography. ((optional, string) This is a comma separated list of metrics you want to retrieve. Defaults to: ga:visits,ga:bounces,ga:pageviews.)
        """
        def set_Metrics(self, value):
            InputSet._set_input(self, 'Metrics', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password for your Google analytics account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ProfileId input for this choreography. ((required, integer) The Google Analytics profile ID to access (Can be found in the URL when clicking the report from your account).)
        """
        def set_ProfileId(self, value):
            InputSet._set_input(self, 'ProfileId', value)

        """
        Set the value of the Segment input for this choreography. ((optional, string) Used to segment your data by dimensions and/or metrics. You can use expressions for segments just as you would for the Filters parameter.)
        """
        def set_Segment(self, value):
            InputSet._set_input(self, 'Segment', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) Indicates the sorting order and direction for the returned data. Values can be separated by commas (i.e. ga:browser,ga:pageviews).)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)

        """
        Set the value of the StartDate input for this choreography. ((required, date) The start date for the range of data to retrieve. Use epoch timestamp in milliseconds or formatted as yyyy-MM-dd.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the StartIndex input for this choreography. ((optional, integer) The starting entry for the feed. Defaults to 1.)
        """
        def set_StartIndex(self, value):
            InputSet._set_input(self, 'StartIndex', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The username for your Google analytics account.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetMetrics choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetMetricsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The full response from Google Analytics.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Bounces" output from this choreography execution. ((integer) The bounces metrics parsed from the Google Analytics response)
        """
        def get_Bounces(self):
            return self._output.get('Bounces', None)
        """
        Retrieve the value for the "PageViews" output from this choreography execution. ((integer) The page views parsed from the Google Analytics response)
        """
        def get_PageViews(self):
            return self._output.get('PageViews', None)
        """
        Retrieve the value for the "Visits" output from this choreography execution. ((integer) The visits metrics parsed from the Google Analytics response.)
        """
        def get_Visits(self):
            return self._output.get('Visits', None)

class GetMetricsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMetricsResultSet(response, path)
