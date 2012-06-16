
###############################################################################
#
# CampaignStats
# Retrieve campaign stats by ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CampaignStats(Choreography):

    """
    Create a new instance of the CampaignStats Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AdMob/CampaignStats')


    def new_input_set(self):
        return CampaignStatsInputSet()

    def _make_result_set(self, result, path):
        return CampaignStatsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CampaignStatsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CampaignStats
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CampaignStatsInputSet(InputSet):
        """
        Set the value of the CampaignID input for this choreography. ((required, string) Search for ad campaigns using this ID.)
        """
        def set_CampaignID(self, value):
            InputSet._set_input(self, 'CampaignID', value)

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
        Set the value of the ObjectDimension input for this choreography. ((optional, string) Specify a campaign to group and narrow your search.)
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
A ResultSet with methods tailored to the values returned by the CampaignStats choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CampaignStatsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from AdMob in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CampaignStatsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CampaignStatsResultSet(response, path)
