
###############################################################################
#
# FederalGrants
# Returns information about federal grants awarded.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FederalGrants(Choreography):

    """
    Create a new instance of the FederalGrants Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/FederalGrants')


    def new_input_set(self):
        return FederalGrantsInputSet()

    def _make_result_set(self, result, path):
        return FederalGrantsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FederalGrantsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FederalGrants
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FederalGrantsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API key provided by Sunlight Data Services.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AgencyName input for this choreography. ((optional, string) Full-text search on the reported name of the federal agency awarding the grant.)
        """
        def set_AgencyName(self, value):
            InputSet._set_input(self, 'AgencyName', value)

        """
        Set the value of the Amount input for this choreography. ((optional, string) The grant amount. Valid formats include: 500 (exactly $500); >|500 (greater than, or equal to 500); <|500 (less than or equal to 500).)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the AssistanceType input for this choreography. ((optional, integer) A numeric code for the type of grant awarded. See documentation for more details for this parameter.)
        """
        def set_AssistanceType(self, value):
            InputSet._set_input(self, 'AssistanceType', value)

        """
        Set the value of the FiscalYear input for this choreography. ((optional, date) The year in which the grant was awarded. A YYYY formatted year. You can also specify a range by separating years with a pipe (i.e. 2008|2012).)
        """
        def set_FiscalYear(self, value):
            InputSet._set_input(self, 'FiscalYear', value)

        """
        Set the value of the RecipientName input for this choreography. ((optional, string) Full-text search on the reported name of the grant recipient.)
        """
        def set_RecipientName(self, value):
            InputSet._set_input(self, 'RecipientName', value)

        """
        Set the value of the RecipientState input for this choreography. ((optional, string) Two-letter abbreviation of the state in which the grant was awarded.)
        """
        def set_RecipientState(self, value):
            InputSet._set_input(self, 'RecipientState', value)

        """
        Set the value of the RecipientType input for this choreography. ((optional, integer) The numeric code representing the type of entity that received the grant. See documentation for more details about this parameter.)
        """
        def set_RecipientType(self, value):
            InputSet._set_input(self, 'RecipientType', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Indicates the desired format for the response. Accepted values are: json (the default), csv, and xls. Note when specifying xls, restults are returned as Base64 encoded data.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the FederalGrants choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FederalGrantsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Influence Explorer. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FederalGrantsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FederalGrantsResultSet(response, path)
