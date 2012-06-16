
###############################################################################
#
# AdGroupStats
# Search for Ad Group statistics by entering their IDs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AdGroupStats(Choreography):

    """
    Create a new instance of the AdGroupStats Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AdMob/AdGroupStats')


    def new_input_set(self):
        return AdGroupStatsInputSet()

    def _make_result_set(self, result, path):
        return AdGroupStatsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AdGroupStatsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AdGroupStats
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AdGroupStatsInputSet(InputSet):
        """
        Set the value of the AdGroupID input for this choreography. ((required, string) Search for ad groups using this ID.)
        """
        def set_AdGroupID(self, value):
            InputSet._set_input(self, 'AdGroupID', value)

        """
        Set the value of the ClientKey input for this choreography. ((required, string) Enter user client key.)
        """
        def set_ClientKey(self, value):
            InputSet._set_input(self, 'ClientKey', value)

        """
        Set the value of the EndDate input for this choreography. ((required, date) Enter search end date in following format: 2011-09-12)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the ObjectDimension input for this choreography. ((optional, string) Specify an Ad group to narrow your search.)
        """
        def set_ObjectDimension(self, value):
            InputSet._set_input(self, 'ObjectDimension', value)

        """
        Set the value of the OrderBy input for this choreography. ((optional, string) Order by the number of impressions. Example: [impressions]=asc)
        """
        def set_OrderBy(self, value):
            InputSet._set_input(self, 'OrderBy', value)

        """
        Set the value of the StartDate input for this choreography. ((required, date) Enter search start date in following format: 2011-09-12)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the TimeDimension input for this choreography. ((optional, string) Specify whether stats should be grouped by day, week, or month.)
        """
        def set_TimeDimension(self, value):
            InputSet._set_input(self, 'TimeDimension', value)

        """
        Set the value of the Token input for this choreography. ((required, string) Enter user token.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the AdGroupStats choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AdGroupStatsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from AdMob in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AdGroupStatsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AdGroupStatsResultSet(response, path)
