
###############################################################################
#
# NewCandidates
# Retrieves 20 of the most recently added political office candidates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class NewCandidates(Choreography):

    """
    Create a new instance of the NewCandidates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/CampaignFinance/Candidates/NewCandidates')


    def new_input_set(self):
        return NewCandidatesInputSet()

    def _make_result_set(self, result, path):
        return NewCandidatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return NewCandidatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the NewCandidates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class NewCandidatesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CampaignCycle input for this choreography. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year. )
        """
        def set_CampaignCycle(self, value):
            InputSet._set_input(self, 'CampaignCycle', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Enter json or xml.  Default is json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the NewCandidates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class NewCandidatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class NewCandidatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return NewCandidatesResultSet(response, path)
