
###############################################################################
#
# GetRateSummary
# Retrieve current interest rates for a specified loan type.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRateSummary(Choreography):

    """
    Create a new instance of the GetRateSummary Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zillow/GetRateSummary')


    def new_input_set(self):
        return GetRateSummaryInputSet()

    def _make_result_set(self, result, path):
        return GetRateSummaryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRateSummaryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRateSummary
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRateSummaryInputSet(InputSet):
        """
        Set the value of the OutputFormat input for this choreography. ((optional, string) Enter the desired query output format.  Enter: xml, or json.  Default output is set to: xml.)
        """
        def set_OutputFormat(self, value):
            InputSet._set_input(self, 'OutputFormat', value)

        """
        Set the value of the State input for this choreography. ((optional, string) Enter a U.S. state abbreviation for which to retrieve mortgage rates.  If null, the national average rate is returned.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the ZWSID input for this choreography. ((required, string) Enter a Zillow Web Service Identifier (ZWS ID).)
        """
        def set_ZWSID(self, value):
            InputSet._set_input(self, 'ZWSID', value)


"""
A ResultSet with methods tailored to the values returned by the GetRateSummary choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRateSummaryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zillow.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRateSummaryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRateSummaryResultSet(response, path)
