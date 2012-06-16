
###############################################################################
#
# CommitteeIndependentExpenditures
# Retrieve the 20 most recent independent expenditures by a given committee, also known as "Super PACs."
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CommitteeIndependentExpenditures(Choreography):

    """
    Create a new instance of the CommitteeIndependentExpenditures Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/CampaignFinance/IndependentExpenditures/CommitteeIndependentExpenditures')


    def new_input_set(self):
        return CommitteeIndependentExpendituresInputSet()

    def _make_result_set(self, result, path):
        return CommitteeIndependentExpendituresResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CommitteeIndependentExpendituresChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CommitteeIndependentExpenditures
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CommitteeIndependentExpendituresInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CampaignCycle input for this choreography. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year.)
        """
        def set_CampaignCycle(self, value):
            InputSet._set_input(self, 'CampaignCycle', value)

        """
        Set the value of the FECID input for this choreography. ((required, string) Enter the FEC ID for the committee.  ID can be obtained by first running the CommitteeSearch Choreo.)
        """
        def set_FECID(self, value):
            InputSet._set_input(self, 'FECID', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) The first 20 results are shown by default. To page through the results, set Offset to the appropriate value (e.g., Offset=40 displays results 41–60).)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Enter json or xml.  Default is json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the CommitteeIndependentExpenditures choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CommitteeIndependentExpendituresResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CommitteeIndependentExpendituresChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CommitteeIndependentExpendituresResultSet(response, path)
