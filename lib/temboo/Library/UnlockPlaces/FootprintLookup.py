
###############################################################################
#
# FootprintLookup
# Retrieves the footprint for a specified place identifier.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FootprintLookup(Choreography):

    """
    Create a new instance of the FootprintLookup Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/UnlockPlaces/FootprintLookup')


    def new_input_set(self):
        return FootprintLookupInputSet()

    def _make_result_set(self, result, path):
        return FootprintLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FootprintLookupChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FootprintLookup
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FootprintLookupInputSet(InputSet):
        """
        Set the value of the Format input for this choreography. ((optional, string) The format of the place search results. One of xml, kml, json, georss or txt. Defaults to "xml".)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the Gazetteer input for this choreography. ((optional, string) The place-name source to take locations from. The options are geonames, os, naturalearth or unlock which combines all the previous. Defaults to "unlock".)
        """
        def set_Gazetteer(self, value):
            InputSet._set_input(self, 'Gazetteer', value)

        """
        Set the value of the Identifier input for this choreography. ((required, integer) The place identifier that you want to use for the search. Note that this identifier is returned in the <geometryRef> response element of other Unlock Places search Choreos.)
        """
        def set_Identifier(self, value):
            InputSet._set_input(self, 'Identifier', value)

        """
        Set the value of the MaxRows input for this choreography. ((optional, integer) The maximum number of results to return. Defaults to 20. Cannot exceed 1000.)
        """
        def set_MaxRows(self, value):
            InputSet._set_input(self, 'MaxRows', value)

        """
        Set the value of the StartRow input for this choreography. ((optional, integer) The row to start results display from. Defaults to 1.)
        """
        def set_StartRow(self, value):
            InputSet._set_input(self, 'StartRow', value)


"""
A ResultSet with methods tailored to the values returned by the FootprintLookup choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FootprintLookupResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Unlock. Defaults to XML based on the format input parameter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FootprintLookupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FootprintLookupResultSet(response, path)
