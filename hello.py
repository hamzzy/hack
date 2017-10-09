class	Not:
 def get_output(self):
   if self._input	is	None:
       return None
   value=self._input.get_output()
   if value is None:
       return	None
   return not value
